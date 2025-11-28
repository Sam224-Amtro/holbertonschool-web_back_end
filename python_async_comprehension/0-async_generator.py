#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate a random number every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
