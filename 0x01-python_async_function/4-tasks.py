#!/usr/bin/env python3
""" module code.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Tasks"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    all_delays = []
    for delay_task in asyncio.as_completed(delays):
        earliest_result = await delay_task
        all_delays.append(earliest_result)
    return all_delays
