#!/usr/bin/env python3
""" module code.
"""
from typing import List
import asyncio


async def task_wait_random(max_delay: int) -> float:
    """Returns a random delay between 0 and max_delay (inclusive)"""
    # Implementation omitted for brevity

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
