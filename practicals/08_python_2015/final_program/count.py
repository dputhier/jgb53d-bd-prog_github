# -*- coding: utf-8 -*-

"""
This program count the number of transcripts.
"""

# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

from utils import get_tx_name

def count(file_name):
    """Count the number of transcript."""
    # Pensez à adapter le chemin vers le fichier.
    # Ici, il est dans le dossier data présent dans le
    # répertoire supérieur
    file_handler = open(file_name, "r")


    # ***
    # Ce dictionnaire contiendra l'ensemble des transcrits (tx)
    dict_of_tx_name = dict()

    # On utilise une boucle for pour
    # lire des lignes renvoyées par l'objet
    # file_handler
    for line in file_handler:

        # get transcript name
        tx_name = get_tx_name(line)

        # Si le transcrit n'est pas dans la liste, on l'ajoute
        # ***
        if tx_name not in dict_of_tx_name:
            # ***
            # On déclare une nouvelle clef dans le dictionnaire
            # et on place sa valeur à 1.
            dict_of_tx_name[tx_name] = 1


    # Après être sorti de la boucle
    # on imprime le nombre de transcrits.
    # len(tx_list) est un entier (int) qui correspond au nombre de
    # clef du dictionnaire. Pour pouvoir le concatener
    # avec une chaîne de caractères (le message), il faut le transformer
    # en chaîne de caractères (str()).
    print("Le nombre de transcrits est: " + str(len(dict_of_tx_name)))  #  n = 5000



if __name__ == "__main__":

    count("../data/hg38_5k.gtf")
