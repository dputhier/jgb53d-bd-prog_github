# -*- coding: utf-8 -*-
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

"""
    Author D. Puthier
    date: Wed Oct 28 16:44:29 CET 2015
    program: tx_len.py
    This program is intended to compute the genomic coverage of transcripts (exon
    + intron length).
"""

# On importe le module re
# afin de pouvoir rechercher
# une expression régulière dans une
# chaîne de caractères.
import re

# Ce dictionnaire contiendra les coordonnées de
# départ (start) des transcrits

transcript_starts = dict()

# Ce dictionnaire contiendra les coordonnées de
# fin (end) des transcrits
transcript_ends = dict()


# Pensez à adapter le chemin vers le fichier.
# Ici, il est dans le dossier data présent dans le
# répertoire supérieur

file_handler = open("../data/hg38_5k.gtf", "r")


# On utilise une boucle for pour
# lire des lignes renvoyées par l'objet
# file_handler
for line in file_handler:

    # On découpe la ligne sur le séparateur "\t"

    columns = line.split("\t")

    # On récupère le start et le end du transcrit courant

    start_current = int(columns[3]) # attention au type
    end_current = int(columns[4]) # attention au type



    # On substitue dans la colonne 9 n'importe quel caractère (.)
    # répété 0 fois ou plus (*) et
    # suivit de transcript_id, d'un espace et d'un double guillemet par
    # une chaine de caractères vide ("").

    tx_name = re.sub('.* transcript_id "', "", columns[8])

    # On substitue tout ce qui se trouve à droite du nom du transcrit: un guillemet suivit de
    # n'importe quel caractère (.) répété 0 fois ou plus (*) et d'un caractère retour à la ligne.
    tx_name = re.sub('".*\n', "", tx_name)


    # Si le transcript n'est pas dans transcript_starts
    # il n'est pas non plus dans les autres dictionnaires.
    # On les initialise.
    if not transcript_starts.get(tx_name):

        transcript_starts[tx_name] = start_current
        transcript_ends[tx_name] = end_current

    else:
        # Sinon le start est plus petit que le start connu,
        # on le conserve.
        if start_current < transcript_starts[tx_name]:

            transcript_starts[tx_name] = start_current

        # Si le end est plus grand que celui connu pour ce transcrit,
        # On le conserve.
        if end_current > transcript_ends[tx_name]:

            transcript_ends[tx_name] = end_current

# Pour toutes les clefs du dictionnaire transcript_starts

for tx_name in transcript_starts:

    print(tx_name + "\t" + str(transcript_ends[tx_name] - transcript_starts[tx_name] + 1))
