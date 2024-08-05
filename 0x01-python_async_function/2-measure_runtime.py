#!/usr/bin/env python3
""" module code.
"""
import asyncio
import time


# Import the wait_n function from the '1-concurrent_coroutines' module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of the wait_n function.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time taken per coroutine execution.
    """
    # Record the start time
    start_time = time.time()

    # Run the wait_n function with the given arguments
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Calculate and return the average time per coroutine execution
    return total_time / n
