#!/usr/bin/env python3
""" module.
"""
from typing import List
import importlib

async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates a list  from a  generator."""
    return [num async for num in async_generator()]
