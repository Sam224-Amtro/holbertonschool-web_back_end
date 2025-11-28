#!/usr/bin/env python3
""" Exécutons plusieurs coroutines en même temps avec async """
import asyncio
import random


async def async_generator():
    """
    Génère de façon asynchrone 10 nombres aléatoires entre 0 et 10.

    Yields:
        float: Un nombre aléatoire compris entre 0 et 10.
    """
    for _ in range(10):
        # Attend 1 seconde de manière asynchrone
        await asyncio.sleep(1)
        # Retourne un nombre aléatoire (float) entre 0 et 10
        yield random.uniform(0, 10)
