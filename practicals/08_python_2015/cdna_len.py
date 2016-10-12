# -*- coding: utf-8 -*-
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

"""
    Author D. Puthier
    date: Wed Oct 28 16:44:29 CET 2015
    program: cdna_len.py
    This program is intended to compute the number of exons in the gtf file.
    """
# On importe le module re
# afin de pouvoir rechercher
# une expression régulière dans une
# chaîne de caractères.

from utils import get_tx_name

def cdna_len_cmd(file_name):
    """Compute the cDNA length of a transcript."""

    cdna_len_dict = dict()


    file_handler = open(file_name, "r")

    for line in file_handler:

        # On découpe la ligne sur le séparateur "\t"

        columns = line.split("\t")
        start = int(columns[3])
        end = int(columns[4])
        tx_size = end - start + 1
        
        if columns[2] == "exon":

            # retrieve tx_name

            tx_name = get_tx_name(columns[8])

            # Si le transcript n'est pas connu dans le dictionnaire
            # On l'initialise
            if not cdna_len_dict.get(tx_name):

                cdna_len_dict[tx_name] = tx_size


            else:
                # Sinon on ajoute 1 à la valeur associée à la clef
                # tx_name

                cdna_len_dict[tx_name] += tx_size

    # Pour toutes les clefs du dictionnaire cdna_len

    for tx_name in cdna_len_dict:

        print(tx_name + "\t" + str(cdna_len_dict[tx_name]))

if __name__ == "__main__":

    cdna_len_cmd("../data/hg38_5k.gtf")
