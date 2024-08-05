#!/usr/bin/env python3
""" module code.
"""


from typing import List
import asyncio


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ times with the specified 'max_delay', and returns a list
    """
    delays = []
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

# Function to be imported
async def task_wait_random(max_delay: int) -> float:
    """ Waits for random delay between 0 -'max_delay' and returns the delay.
    """
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
