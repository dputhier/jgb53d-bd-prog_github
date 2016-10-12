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
import re

# Ce dictionnaire contiendra le nombre d'exon de chaque transcrit

nb_exons = dict()


# Pensez à adapter le chemin vers le fichier.

file_handler = open("../data/refGene_hg38.gtf", "r")


# On utilise une boucle for pour
# lire des lignes renvoyées par l'objet
# file_handler

for line in file_handler:
    
    # On découpe la ligne sur le séparateur "\t"
    
    columns = line.split("\t")
    
    if columns[2] == "exon":
        
        # On substitue dans la colonne 9 n'importe quel caractère (.)
        # répété 0 fois ou plus (*) et
        # suivit de transcript_id, d'un espace et d'un double guillemet par
        # une chaine de caractères vide ("").
        
        tx_name = re.sub('.* transcript_id "', "", columns[8])
        
        # On substitue tout ce qui se trouve à droite du nom du transcrit: un guillemet suivit de
        # n'importe quel caractère (.) répété 0 fois ou plus (*) et d'un caractère retour à la ligne.
        tx_name = re.sub('".*\n', "", tx_name)
        
        
        # Si le transcript n'est pas connu dans le dictionnaire
        # On l'initialise à 1 pour la clef tx_name.
        if not nb_exons.get(tx_name):
            
            nb_exons[tx_name] = 1
    
    
        else:
            # Sinon on ajoute 1 à la valeur associée à la clef
            # tx_name
            
            nb_exons[tx_name] += 1

# Pour toutes les clefs du dictionnaire nb_exons

for tx_name in nb_exons:
    
    print(tx_name + "\t" + str(nb_exons[tx_name]))