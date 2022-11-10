"""
Decorators for DevTed
"""
from .typing import Vector


def zipparams(ignore: Vector = None):
    """
    Zips all kwargs to zip_params and
    passes this obj as keyword to the function
    """
    def decorator(func):
        def wrapper(**kwargs):
            zip_params = {k: v for k, v in kwargs.items() if k not in ignore}
            return func(zip_params=zip_params, **kwargs)
        return wrapper
    return decorator
