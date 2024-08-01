#!/usr/bin/env python3
"""Module for summing mixed numeric lists.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all elements in a list of integers and floats.
    """
    return sum(map(float, mxd_lst))
