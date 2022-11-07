"""
Decorators for DevTed
"""
from ._typing import Vector


def zipparams(ignore: Vector = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            zip_params = {k: v for k, v in kwargs.items() if k not in ignore}
            return func(zip_params=zip_params, **kwargs)
        return wrapper
    return decorator
