import os
import json
import sys

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient

from cloudstore.abstract_store import CloudStore
from cloudstore.utils import multi_thread
from cloudstore.utils import gen_random_name
from cloudstore.logger import logger


class AZRStore(CloudStore):
    """azure cloud store."""

    def __init__(self):
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        if connect_str is None:
            logger.error("AZURE_STORAGE_CONNECTION_STRING env variable not set")
            sys.exit(1)
        try:
            AZRStore.client = BlobServiceClient.from_connection_string(connect_str)
        except ValueError:
            logger.error("AZURE_STORAGE_CONNECTION_STRING string malformed, check the env variable.")
            sys.exit(1)
        self.client = AZRStore.client

    def create_bucket(self, bucket):
        container_client = self.client.create_container(bucket)
        logger.info("bucket : {} created".format(container_client))
        return container_client

    def delete_bucket(self, bucket):
        container_client = self.client.get_container_client(bucket)
        container_client.delete_container()

    @multi_thread
    def upload(self, bucket: str, file_name: str):
        blob_client = self.client.get_blob_client(container=bucket, blob=file_name)
        with open(file_name, "rb") as fh:
            blob_client.upload_blob(fh)

    @multi_thread
    def download(self, bucket, object_name, file_name):
        blob_client = self.client.get_blob_client(container=bucket, blob=object_name)
        blob = blob_client.download_blob()
        data = blob.readall()
        with open(file_name, "wb") as fh:
            fh.write(data)
