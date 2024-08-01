#!/usr/bin/env python3
"""
This module provides a function that takes a tuple of integers
and a factor as input, and returns a list of integers where each
element from the original tuple is repeated the specified number
of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Multiplies each element in the input tuple by the given factor
    and returns a new list containing the repeated elements.

    Args:
        lst (Tuple): The input tuple of integers.
        factor (int, optional): The number of times each element
            should be repeated. Defaults to 2.

    Returns:
        List: A new list containing the repeated elements from
            the input tuple.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
