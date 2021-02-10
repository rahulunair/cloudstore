from concurrent.futures import ProcessPoolExecutor as ppe
from concurrent.futures import ThreadPoolExecutor as tpe
from functools import wraps
from os import read
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


def compress(files, tar_file):
    """compress a file."""
    if not isinstance(files, list):
        files = [files]
    status = tqdm.tqdm(files)
    with tarfile.open(tar_file, mode="w:gz") as tf:
        for f in files:
            tf.add(f)
            status.set_description(f"compressing {f} in progress")


if __name__ == "__main__":
    compress("./logger.py", "logger")
