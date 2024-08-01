#!/usr/bin/env python3
"""Module for creating a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number by a specified multiplier.
    Args: multiplier (float): The value to multiply the input number with.
    Returns:  Callable[[float], float]: A function that
    takes a float and returns a float.
    """
    return lambda x: x * multiplier
