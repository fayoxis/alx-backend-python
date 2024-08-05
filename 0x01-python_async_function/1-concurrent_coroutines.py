#!/usr/bin/env python3
"""Task 1's module."""
import asyncio
from typing import List

from utils import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    wait_times = [await task for task in asyncio.as_completed(tasks)]
    return sorted(wait_times)
