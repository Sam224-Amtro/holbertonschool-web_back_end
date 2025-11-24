#!/usr/bin/env python3
"""
Annotations pour une fonction qui renvoie le plancher d'un nombre.
"""
import math
from typing import Any


def floor(n: float) -> int:
    """
    Returns le plancher d'un flotteur sous forme d'entier.

    Args:
        n (float): Le numéro flottant au sol.

    Returns:
        int: La valeur entière plancher du float.
    """
    return math.floor(n)
