"""
Main entrypoint
---------------
Just-in-time injections awaitable from asyncio coroutines

Author: Chris Lee
Email: chrisklee93@gmail.com
"""
from typing import Type, Union, Callable


class Injection:
    pass


def injected(fn_or_cls: Union[Callable, Type]):
    """
    Decorator that signifies the following class or callable is injection aware
    """
    if isinstance(fn_or_cls, type):
        pass
    elif callable(fn_or_cls):
        pass
    else:
        raise ValueError(("injected must be called on a class or function"))


def injection(name: str = None):
    """
    Decorator that signifies the decorated function is an injection
    """

    # If decorator is used without arguments
    if callable(name):
        fn = name
        name = fn.__name__

    def wrapped(fn):
        global name
        if not name:
            name = fn.__name__
        return fn

    return wrapped


def inject():
    pass
