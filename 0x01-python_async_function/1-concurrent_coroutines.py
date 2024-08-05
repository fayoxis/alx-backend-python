#!/usr/bin/env python3
""" modules code ."""
import asyncio
from typing import List

from utils import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes unknown times."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
