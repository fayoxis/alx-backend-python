#!/usr/bin/env python3
"""Module for creating a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number
    """
    return lambda x: x * multiplier
