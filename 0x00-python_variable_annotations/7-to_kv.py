#!/usr/bin/env python3
""" Complex types - string and int/float to tuple module """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v and returns a tuple
    with k and the square of v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing k and the square
        of v as a float.
    """
    return (k, float(v ** 2))
