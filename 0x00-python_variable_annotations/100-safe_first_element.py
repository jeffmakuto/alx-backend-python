#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input sequence if it
    exists, otherwise returns None.

    Args:
        lst (Sequence): Any sequence.

    Returns:
        Union[Any, None]: The first element of the sequence
        if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
