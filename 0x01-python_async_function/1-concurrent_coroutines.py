#!/usr/bin/env python3
""" module code."""
import asyncio
from typing import List

from utils import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes unknow  times."""
    wait_times = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
    )
    return sorted(wait_times)
