import json
import sys

#import azure.storage.blob as azure_store

from cloudstore.abstract_store import CloudStore
from cloudstore.utils import multi_thread
from cloudstore.utils import gen_random_name
from cloudstore.logger import logger


class AZRStore(CloudStore):
    """azure cloud store."""

    def upload(self, bucket: str, file_name) -> str:
        pass

    def download(self, bucket, object_name, file_name):
        pass
