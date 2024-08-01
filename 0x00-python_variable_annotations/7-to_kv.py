#!/usr/bin/env python3
"""Modules."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key and its value to a tuple.
    Args:
        k (str): The key.
        v (Union[int, float]): The value, either an integer or float.
    
    Returns:
        Tuple[str, float]: A tuple containing the key and the square of its value.
    """
    return (k, float(v * v))
