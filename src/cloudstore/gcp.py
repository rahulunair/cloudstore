import json
import sys

from google.cloud import storage as google_store
from google.api_core.exceptions import NotFound as GCS_NotFound
from google.api_core.exceptions import Forbidden as GCS_Forbidden
from google.auth.exceptions import DefaultCredentialsError as GCSCREDError

from cloudstore.abstract_store import CloudStore
from cloudstore.utils import multi_thread
from cloudstore.utils import gen_random_name
from cloudstore.logger import logger


class GCStore(CloudStore):
    """google cloud store."""

    def __init__(self):
        super().__init__()
        try:
            GCStore.client = google_store.Client()
            self.client = GCStore.client
        except GCSCREDError as e:
            logger.error(
                (
                    "\ncredentials file is expected"
                    "\nuse: GOOGLE_APPLICATION_CREDENTIALS env var to set the path to the credential file"
                    "\nsee: https://cloud.google.com/docs/authentication/getting-started#setting_the_environment_variable"
                )
            )
            logger.error("credentials not given, exiting..")
            sys.exit(1)

    def create_bucket(self, bucket_name: str):
        """create a new bucket"""
        bucket = self.client.bucket(bucket_name)
        bucket.storage_class = "COLDLINE"
        try:
            new_bucket = self.client.create_bucket(bucket, location="us")
        except GCS_Forbidden:
            new_bucket = self.client.create_bucket(
                "bucket_" + gen_random_name(), location="us"
            )
        logger.info(
            "created new bucket {} in {} with storage class {}".format(
                new_bucket.name, new_bucket.location, new_bucket.storage_class
            )
        )
        return new_bucket

    @multi_thread
    def upload(self, bucket_name: str, file_name):
        """upload file to google cloud."""
        create_b = False
        try:
            bucket = self.client.get_bucket(bucket_name)
        except GCS_Forbidden:
            logger.error(
                "you dont have access, to the bucket, trying to create a new one.."
            )
            create_b = True
        except GCS_NotFound as e:
            logger.error("bucket name not found, trying to create a new one")
            logger.error("exception: {}".format(e))
            create_b = True
        if create_b:
            bucket = self.create_bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_name)
        logger.info("file saved, URL:{}".format(blob.public_url))
        return json.dumps(
            dict(
                bucket_name=blob.bucket.name,
                object_name=blob.name,
                public_url=blob.public_url,
            )
        )

    @multi_thread
    def download(self, bucket, object_name, file_name):
        bucket = self.client.get_bucket(bucket)
        blob = bucket.get_blob(object_name)
        blob.download_to_filename(file_name)
        return json.dumps(dict(object_name=blob.name, file_name=file_name))
