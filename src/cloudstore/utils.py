"""utilities for cloudstore."""

from concurrent.futures import ProcessPoolExecutor as ppe
from concurrent.futures import ThreadPoolExecutor as tpe
from functools import wraps
import random
import tarfile

import tqdm


def multi_thread(func):
    """multi thread a function."""

    @wraps(func)
    def mt_func(*args, **kwargs):
        return tpe().submit(func, *args, **kwargs)

    return mt_func


def multi_process(func):
    """multi process a function."""

    @wraps(func)
    def mp_func(*args, **kwargs):
        return ppe().submit(func, *args, **kwargs)

    return mp_func


def gen_random_name(size=6):
    """random names"""
    return "".join(
        random.choice("aeiou" if x % 2 else "bcdfghklmnpqrstvwxyz") for x in range(size)
    )


@multi_thread
def compress(files, tar_file):
    """compress a file."""
    if not isinstance(files, list):
        files = [files]
    status = tqdm.tqdm(files)
    with tarfile.open(tar_file + ".tar.gz", mode="w:gz") as tr_file:
        for member in files:
            tr_file.add(member)
            status.set_description(f"compressing {member} in progress")


@multi_thread
def decompress(tar_file):
    """decompress a tar gz file."""
    with tarfile.open(tar_file) as tr_file:
        for member in tqdm.tqdm(
            iterable=tr_file.getmembers(), total=len(tr_file.getmembers())
        ):
            tr_file.extract(member=member)
