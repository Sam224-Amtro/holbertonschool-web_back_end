#!/usr/bin/env python3
"""Fonction – créer un multiplicateur."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Retourne une fonction qui multiplie un nombre par `multiplier`."""
    def multiplier_func(x: float) -> float:
        """Multiplier un nombre par le multiplicateur."""
        return x * multiplier
    return multiplier_func
