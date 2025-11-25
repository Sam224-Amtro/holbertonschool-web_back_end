#!/usr/bin/env python3
"""Fonction pour la liste mixte"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Prend une liste d'entiers et de nombres à virgule flottante et
    renvoie leur somme sous forme de nombre à virgule flottante.
    """
    return float(sum(mxd_lst))
