from typing import List
import asyncio

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    delays = []
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

async def task_wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.
    """
    import random
    import asyncio
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
