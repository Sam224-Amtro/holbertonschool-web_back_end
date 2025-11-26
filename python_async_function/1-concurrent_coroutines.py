#!/usr/bin/env python3
"""
Module pour l'exécution concurrente de tâches asynchrones avec des délais aléatoires.
"""
import asyncio
from typing import List
from random import uniform

async def wait_random(max_delay: int) -> float:
    """
    Attend un délai aléatoire compris entre 0 et max_delay secondes.

    Args:
        max_delay (int): délai maximum en secondes

    Returns:
        float: le délai utilisé
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance wait_random n fois de manière concurrente et retourne
    la liste des délais obtenus dans l'ordre d'achèvement.

    Args:
        n (int): nombre d'appels à wait_random
        max_delay (int): délai max pour chaque appel

    Returns:
        List[float]: liste des délais obtenus
    """
    # Crée n coroutines wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]

    # asyncio.as_completed renvoie les résultats au fur et à mesure
    results = []
    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)

    return results
