#!/usr/bin/env python3
"""Fonction qui convertit une clé et une valeur en un tuple."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne un tuple où la clé est k et la valeur est le carré de v en float.
    """
    return (k, float(v ** 2))
