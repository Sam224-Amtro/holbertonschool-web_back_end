#!/usr/bin/env python3
from math import floor as math_floor
from typing import Callable


def floor(n: float) -> int:
    """
    Renvoie le plancher du float donné.

    Args:
    n (float): le numéro flottant à plancher.

    Retours:
    int: Le plus grand entier inférieur ou égal à n.
    """
    return math_floor(n)
