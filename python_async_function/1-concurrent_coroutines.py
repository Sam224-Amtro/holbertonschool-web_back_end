#!/usr/bin/env python3
"""
Module for basic async syntax -
wait_random  & wait_n coroutine
"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Générez wait_random n fois et revenez"""
    """liste des retards par ordre croissant."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
