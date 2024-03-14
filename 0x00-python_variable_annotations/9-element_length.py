#!/usr/bin/env python3
""" Let's duck type an iterable object module """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences as input and returns a list of tuples
    where each tuple contains an element from the input list along with
    its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains an element from the input list along with its length.
    """
    return [(i, len(i)) for i in lst]
