#!/usr/bin/env python3
"""module."""

import asyncio
import time
from importlib import import_module


module = import_module('1-async_comprehension')
async_comprehension_module = module
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measures
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
