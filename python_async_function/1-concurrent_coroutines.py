#!/usr/bin/env python3
"""
Module pour l'exécution concurrente de tâches asynchrones avec des délais aléatoires.
"""
import asyncio
from typing import List

# On importe la fonction wait_random depuis le module 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance wait_random n fois et retourne la liste des délais.

    Args:
        n (int): Nombre de fois que wait_random doit être exécuté
        max_delay (int): Délai maximum pour chaque appel à wait_random

    Returns:
        List[float]: Liste des délais obtenus, triée par ordre croissant
    """
    # Crée une liste de tâches asynchrones
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Exécute toutes les tâches simultanément et attend qu'elles se terminent
    delays = await asyncio.gather(*tasks)

    # Retourne la liste des délais triée par ordre croissant
    return sorted(delays)
