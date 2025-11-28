#!/usr/bin/env python3
"""Exécutons plusieurs coroutines en même temps avec async"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Générez de manière asynchrone 10 nombres aléatoires.

    Cette coroutine boucle 10 fois, en attendant de manière asynchrone
    1 seconde à chaque itération, puis donne un flottant aléatoire
    entre 0 et 10.

    Rendements :
    float : Un nombre aléatoire dans la plage [0, 10).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
