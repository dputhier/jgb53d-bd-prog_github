# -*- coding: utf-8 -*-
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

"""
    Author D. Puthier
    date: Wed Oct 28 16:44:29 CET 2015
    program: nb_exons.py
    This program is intended to compute the number of exons in the gtf file.
    """
# On importe le module re
# afin de pouvoir rechercher
# une expression régulière dans une
# chaîne de caractères.

from utils import get_tx_name

def nb_exons(file_name):
    """Compute the number of exon of a transcript."""

    # Ce dictionnaire contiendra le nombre d'exon de chaque transcrit
    nb_exons_dict = dict()

    # Pensez à adapter le chemin vers le fichier.

    file_handler = open(file_name, "r")


    # On utilise une boucle for pour
    # lire des lignes renvoyées par l'objet
    # file_handler

    for line in file_handler:

        # On découpe la ligne sur le séparateur "\t"

        columns = line.split("\t")

        if columns[2] == "exon":

            # retrieve tx_name

            tx_name = get_tx_name(columns[8])

            # Si le transcript n'est pas connu dans le dictionnaire
            # On l'initialise à 1 pour la clef tx_name.
            if not nb_exons_dict.get(tx_name):

                nb_exons_dict[tx_name] = 1


            else:
                # Sinon on ajoute 1 à la valeur associée à la clef
                # tx_name

                nb_exons_dict[tx_name] += 1

    # Pour toutes les clefs du dictionnaire nb_exons

    for tx_name in nb_exons_dict:

        print(tx_name + "\t" + str(nb_exons_dict[tx_name]))

if __name__ == "__main__":

    nb_exons("../data/hg38_5k.gtf")
