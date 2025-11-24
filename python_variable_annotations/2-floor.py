#!/usr/bin/env python3
from math import floor as math_floor

def floor(n: float) -> int:
    """
    Renvoie le plancher (floor) du nombre flottant donné.

    Args:
        n (float): le nombre flottant dont on veut le plancher.

    Returns:
        int: Le plus grand entier inférieur ou égal à n.
    """
    return math_floor(n)

