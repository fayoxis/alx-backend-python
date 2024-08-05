#!/usr/bin/env python3
'''Task 4's module.
'''
from typing import List
import asyncio
from random import uniform

async def task_wait_random(max_delay: int) -> float:
    """Waits for a random delay between 0 and max_delay (inclusive) and returns it."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
        and returns the list of all the delays (float values)."""
    delays = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
    return delays
