# -*- coding: utf8 -*-

"""
Some utility functions for the project.
"""

# On importe le module re
# afin de pouvoir rechercher
# une expression régulière dans une
# chaîne de caractères.

import re

def get_tx_name(char_string):
    """Get the transcript name from a string."""
    # On substitue dans la colonne 9 n'importe quel caractère (.)
    # répété 0 fois ou plus (*) et
    # suivit de transcript_id, d'un espace et d'un double guillemet par
    # une chaine de caractères vide ("").

    tx_name = re.sub('.* transcript_id "', "", char_string)

    # On substitue tout ce qui se trouve à droite du nom du transcrit: un guillemet suivit de
    # n'importe quel caractère (.) répété 0 fois ou plus (*) et d'un caractère retour
    # à la ligne.
    tx_name = re.sub('".*\n', "", tx_name)

    return tx_name
