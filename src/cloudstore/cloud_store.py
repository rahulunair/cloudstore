"""store dispatcher."""

from cloudstore.stores.aws import AWSStore
from cloudstore.stores.azre import AZRStore
from cloudstore.stores.gcp import GCStore


def store(cloud):
    """cloud store factory."""
    if cloud == "gcp":
        return GCStore()
    elif cloud == "azure":
        return AZRStore()
    elif cloud == "aws":
        return AWSStore()
    else:
        raise NotImplementedError
