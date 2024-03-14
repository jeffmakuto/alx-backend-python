#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats as input and returns
    their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers
        and floats to be summed.

    Returns:
        float: The sum of the elements in the mxd_lst.
    """
    return sum(mxd_lst)
