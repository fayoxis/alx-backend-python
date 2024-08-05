#!/usr/bin/env python3
"""Task 1's module."""
import asyncio
from typing import List

from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times and return sorted wait times."""
    wait_times = []
    for _ in range(n):
        wait_time = await wait_random(max_delay)
        wait_times.append(wait_time)
    return sorted(wait_times)
