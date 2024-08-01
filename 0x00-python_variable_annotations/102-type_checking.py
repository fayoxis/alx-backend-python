#!/usr/bin/env python3
"""
Contains a function that returns a list of integers
multiplied by certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list of integers multiplied by certain factor.

    Args:
        lst (Tuple): A tuple of integers.
        factor (int): An integer representing the multiplication factor.

    Returns:
        List: A list of integers multiplied by the given factor.
    """
    zoomed_list = []
    for item in lst:
        zoomed_list.extend([item] * factor)
    return zoomed_list


array = (12, 72, 91)

zoom_2x = zoom_array(array)
print(zoom_2x)

zoom_3x = zoom_array(array, 3)
print(zoom_3x)
