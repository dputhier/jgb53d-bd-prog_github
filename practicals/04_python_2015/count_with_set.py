# -*- coding: utf-8 -*-
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

# On importe le module re
# afin de pouvoir rechercher
# une expression régulière dans une
# chaîne de caractères.
import re

# Pensez à adapter le chemin vers le fichier.
# Ici, il est dans le dossier data présent dans le
# répertoire supérieur
file_handler = open("../data/hg38_5k.gtf", "r")


# ***
# Cet ensemble contiendra l'ensemble des transcrits (tx)
set_of_tx_name = set()

# On utilise une boucle for pour
# lire des lignes renvoyées par l'objet
# file_handler
for line in file_handler:
    
    # On substitue dans 'line' n'importe quel caractère (.) répété 0 fois ou plus (*) et
    # suivit de transcript_id, d'un espace et d'un double guillemet par
    # une chaine de caractères vide ("").
    tx_name = re.sub('.* transcript_id "', "", line)
    # On substitue tout ce qui se trouve à droite du nom du transcrit: un guillemet suivit de
    # n'importe quel caractère (.) répété 0 fois ou plus (*) et d'un caractère retour à la ligne.
    tx_name = re.sub('".*\n', "", tx_name)
    
    # Si le transcrit n'est pas dans la liste, on l'ajoute
    # ***
    if tx_name not in set_of_tx_name:
        # ***
        # On déclare une nouvelle clef dans le dictionnaire
        # et on place sa valeur à 1.
        set_of_tx_name.add(tx_name) # on utilise la méthode add.


# Après être sorti de la boucle
# on imprime le nombre de transcrits.
# len(tx_list) est un entier (int) qui correspond au nombre de clef du dictionnaire. Pour pouvoir le concatener
# avec une chaîne de caractères (le message), il faut le transformer
# en chaîne de caractères (str()).
print("Le nombre de transcrits est: " + str(len(set_of_tx_name)))  # n = 52047