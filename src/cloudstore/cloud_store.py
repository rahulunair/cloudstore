import abc

class CloudStore(abc.ABC):
    """cloud store abstract class."""

    def __init__(self):
        self.client = None

    @abc.abstractmethod
    def upload(self, bucket: str, file) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def download(self, bucket: str, object_name, file_name):
        raise NotImplementedError
