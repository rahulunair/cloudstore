import json
import sys

import boto3
from botocore.exceptions import ClientError as aws_error

from cloudstore import CloudStore
from cloudstore.utils import multi_thread
from cloudstore.utils import gen_random_name
from cloudstore.logger import logger


class AWSStore(CloudStore):
    """aws cloud store."""

    def upload(self, bucket: str, file) -> str:
        pass

    def download(self, bucket, object_name, file_name):
        pass
