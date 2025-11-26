#!/usr/bin/env python3
"""Fonction qui retourne la longueur de chaque élément d'un iterable."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Retourne une liste de tuples : (élément, longueur)."""
    return [(item, len(item)) for item in lst]
