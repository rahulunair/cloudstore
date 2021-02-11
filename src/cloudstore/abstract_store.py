import abc


class CloudStore(abc.ABC):
    """cloud store abstract class."""

    def __init__(self):
        self.client = None

    @abc.abstractmethod
    def upload(self, bucket: str, file_name: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def download(self, bucket: str, object_name: str, file_name: str):
        raise NotImplementedError
