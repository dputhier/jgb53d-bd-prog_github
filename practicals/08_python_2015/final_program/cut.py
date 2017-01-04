# -*- coding: utf-8 -*-

"""
    This programs cut one column from a file
"""
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

def cut(file_name=None, col_to_print=1, sep="\t"):
    """Print the selected column of file. """
    # On ouvre le fichier
    # Adaptez le chemin en fonction de la localisation du
    # file_handler est un objet 'file'. C'est un objet capable de lire
    # les lignes d'un fichier.

    file_handler = open(file_name, "r")

    # Dans la structure for ci-dessous,
    # line est une variable renvoyée
    # par file_handler. On parcours donc
    # le fichier ligne à ligne

    for line in file_handler:

        # A chaque itération/ligne,
        # On découpe la chaîne de caractère
        # sur le séparateur tabulation (\t).
        column = line.split(sep)
        # column[0] si l'on veut la première colonne
        print(column[col_to_print - 1])


if __name__ == "__main__":

    # Print column 4 by default
    cut("../data/hg38_5k.gtf", 4, "\t")

