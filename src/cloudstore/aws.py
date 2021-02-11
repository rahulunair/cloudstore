import json
import sys

import boto3
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError as aws_error
from cloudstore.abstract_store import CloudStore
from cloudstore.utils import multi_thread
from cloudstore.utils import gen_random_name
from cloudstore.logger import logger


class AWSStore(CloudStore):
    """aws cloud store."""

    def __init__(self):
        super().__init__()
        try:
            AWSStore.client = boto3.client("s3")
            self.client = AWSStore.client
        except aws_error as e:
            logger.error("cannot login to aws")
            logger.info("set credentials using environment variables")
            logger.info(
                "please see: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#environment-variables"
            )

    def create_bucket(self, bucket: str):
        """create bucket with `bucket` as name"""
        try:
            self.client.create_bucket(Bucket=bucket)
        except self.client.meta.client.exceptions.BucketAlreadyExists as e:
            logger.error("failed to create bucket {}".format(e))
            raise RuntimeError

    @multi_thread
    def upload(self, bucket: str, file_name):
        """aws upload file to aws."""
        try:
            self.client.upload_file(file_name, bucket, file_name)
        except S3UploadFailedError:
            try:
                self.create_bucket(bucket)
            except RuntimeError:
                logger.error("runtime error raised, exiting")
                sys.exit(1)
            self.client.upload_file(file_name, bucket, file_name)
        except aws_error as e:
            logger.error("client error: {}".format(e))
            sys.exit(1)
        logger.info("file {} upload to s3".format(file_name))

    @multi_thread
    def download(self, bucket, object_name, file_name):
        """download file from s3 given an object name and bucket."""
        try:
            with open(file_name, "wb") as fh:
                try:
                    self.client.download_file(bucket, object_name, file_name)
                except aws_error as e:
                    logger.error("client error: {}".format(e))
                    sys.exit(1)
        except IOError as e:
            logger.error("io error: {}".format(e))
        logger.info("object: {} downloaded to file: {}".format(object_name, file_name))
