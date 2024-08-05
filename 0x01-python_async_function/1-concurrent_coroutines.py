#!/usr/bin/env python3
"""Task 1's module."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines concurrently and returns the delays."""
    delays = [wait_random(max_delay) for _ in range(n)]
    all_delays = []
    for coro in asyncio.as_completed(delays):
        result = await coro
        all_delays.append(result)
    return all_delays
