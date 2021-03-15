"""pkg init."""

import pkg_resources
from cloudstore.cloud_store import store

version = pkg_resources.get_distribution("cloudstore").version
__version__ = version or "0.2.0"

__all__ = ["store"]
