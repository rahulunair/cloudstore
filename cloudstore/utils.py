from concurrent.futures import ProcessPoolExecutor as ppe
from concurrent.futures import ThreadPoolExecutor as tpe
from functools import wraps
import random
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
    return ''.join(random.choice('aeiou' if x % 2 else 'bcdfghklmnpqrstvwxyz')
                   for x in range(size))


