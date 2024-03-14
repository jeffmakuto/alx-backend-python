#!/usr/bin/env python3
""" More involved type annotations """
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None)\
                -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on
    the given key. If the key exists, returns the
    corresponding value. Otherwise, returns the default value.

    Args:
        dct (Mapping): The dictionary to search for the key.
        key (Any): The key to search for in the dictionary.
        default (Optional[T]): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key
        if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
