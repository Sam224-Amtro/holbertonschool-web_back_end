#!/usr/bin/env python3
# Indique que le script doit être exécuté avec l’interpréteur Python 3.

""" Let's execute multiple coroutines at the same time with async """
# Courte description du script : il montre l'utilisation d'async pour exécuter des coroutines.

import asyncio  # Module permettant de gérer l'exécution asynchrone.
import random   # Permet de générer des nombres aléatoires.
import typing   # Sert ici à annoter le type retourné par le générateur.


async def async_generator() -> typing.Generator[float, None, None]:  # type: ignore
    """
    Générateur asynchrone qui produit un nombre aléatoire entre 0 et 10
    toutes les secondes, pendant 10 itérations.
    """
    for _ in range(10):            # Répète l’opération 10 fois.
        await asyncio.sleep(1)     # Pause asynchrone d'une seconde (n'interrompt pas l'exécution globale du programme).
        yield random.uniform(0, 10)  # Produit un nombre aléatoire entre 0 et 10.
