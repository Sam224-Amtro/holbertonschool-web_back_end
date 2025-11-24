#!/usr/bin/env python3

from typing import List
"""
Import (ici inutilisé) permettant d'annoter des listes, par exemple List[float].
"""

def sum_list(input_list: list[float]) -> float:
    """
    Prend une liste de nombres flottants en entrée et retourne leur somme.

    Paramètres :
        input_list (list[float]) : la liste des nombres à additionner.

    Retour :
        float : le résultat de l'addition de tous les éléments.
    """
    return sum(input_list)
