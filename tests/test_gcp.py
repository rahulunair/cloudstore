import os
import pytest

from cloudstore import store

@pytest.fixture()
def set_env():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "test.json"
    yield
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""



def test_upload(set_env):
    # TODO: implement upload
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cloud = store("gcp")
        pytest_wrapped_e.value  == 1
        return True


def test_download(set_env):
    # TODO: implement download
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        cloud = store("gcp")
        pytest_wrapped_e.value  == 1
        return True
