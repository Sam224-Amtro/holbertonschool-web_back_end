#!/usr/bin/env python3
"""
Module pour la syntaxe de base des fonctions asynchrones – coroutine wait_random.
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine asynchrone qui attend un délai aléatoire
    compris entre 0 et max_delay secondes, puis retourne ce délai.

    Arguments :
        max_delay (int) : Durée maximale de l'attente en secondes (10 par défaut).

    Retourne :
        float : Le délai réellement attendu.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
