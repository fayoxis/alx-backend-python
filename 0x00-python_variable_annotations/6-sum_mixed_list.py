#!/usr/bin/env python3
"""Module for summing mixed numeric lists."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all elements in a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or floats.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(map(float, mxd_lst))
