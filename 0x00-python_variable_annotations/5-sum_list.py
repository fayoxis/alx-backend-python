#!/usr/bin/env python3
"""Module for float list summation."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of floating-point numbers in a list.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return sum(input_list)
