# -*- coding: utf-8 -*-
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

# La colonne qu l'on souhaite imprimer
col_to_print = 4

# On ouvre le fichier
# Adaptez le chemin en fonction de la localisation du
# file_handler est un objet 'file'. C'est un objet capable de lire
# les lignes d'un fichier.

file_handler = open("../data/hg38_5k.gtf", "r")

# Dans la structure for ci-dessous,
# line est une variable renvoyée
# par file_handler. On parcours donc
# le fichier ligne à ligne

for line in file_handler:
    
    # A chaque itération/ligne,
    # On découpe la chaîne de caractère
    # sur le séparateur tabulation (\t).
    column = line.split("\t")
    # column[0] si l'on veut la première colonne
    print(column[ col_to_print - 1])