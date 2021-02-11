from cloudstore.aws import AWSStore
from cloudstore.azure import AZRStore
from cloudstore.gcp import GCStore


def store(cloud="gcp"):
    """cloud store factory."""
    if cloud == "gcp":
        return GCStore()
    elif cloud == "azure":
        raise NotImplementedError
        # return AZRStore()
    elif cloud == "aws":
        return AWSStore()
    else:
        raise NotImplementedError
