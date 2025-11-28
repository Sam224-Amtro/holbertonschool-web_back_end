#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """


import asyncio  # Module permettant de gérer l'exécution asynchrone.
import random   # Permet de générer des nombres aléatoires.
import typing   # Sert ici à annoter le type retourné par le générateur.


async def async_generator() -> typing.Generator[float, None, None]: #type: ignore
    """
    Générateur asynchrone qui produit un nombre aléatoire entre 0 et 10
    toutes les secondes, pendant 10 itérations.
    """
    for _ in range(10):            # Répète l’opération 10 fois.
        # Pause asynchrone d'une seconde (n'interrompt pas l'exécution
        # globale du programme).
        await asyncio.sleep(1)
        # Produit un nombre aléatoire entre 0 et 10.
        yield random.uniform(0, 10)
