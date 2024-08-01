#!/usr/bin/env python3
"""
Contains a function that returns a list of integers
multiplied by certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: tuple, factor: int = 2) -> list:
    """
    Returns a list of integers multiplied by a certain factor.
    """
    zoomed_in = []
    for item in lst:
        zoomed_in.extend([item] * factor)
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
print(zoom_2x)  # Output: [12, 12, 72, 72, 91, 91]

zoom_3x = zoom_array(array, 3)
print(zoom_3x)  # Output: [12, 12, 12, 72, 72, 72, 91, 91, 91]
