#!/usr/bin/env python3
""" module code.
"""
import asyncio
wait_random_func = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return the needed task"""
    task = asyncio.create_task(wait_random_func(max_delay))
    return task
