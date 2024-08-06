#!/usr/bin/env python3
"""module.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates random floats between 0 and 10.
    Waits for 1 second before yielding each value.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
