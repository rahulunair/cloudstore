import os

import pytest

from cloudstore import store


@pytest.fixture()
def env_setup():
    os.environ["AZURE_STORAGE_CONNECTION_STRING"] = "AccountName=42"
    yield
    os.environ["AZURE_STORAGE_CONNECTION_STRING"] = ""

def test_upload(env_setup):
    cloud = store("azure")
    # TODO: test upload
    return True


def test_download(env_setup):
    cloud = store("azure")
    # TODO: test download
    return True
