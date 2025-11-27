#!/usr/bin/env python3
"""contient la fonction task_wait_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée et retourne une asyncio.Task pour la coroutine wait_random.

    Args:
        max_delay (int): Le délai maximal pour la coroutine wait_random.

    Returns:
        asyncio.Task: Un objet Task encapsulant la coroutine wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
