#!/usr/bin/env python3
"""Task 0's module: Waits for a random number of seconds."""


import asyncio
from random import random

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random number of seconds up to max_delay."""
    wait_time = random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
