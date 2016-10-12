# -*- coding: utf-8 -*-
# La ligne précédente permet d'utiliser des caractères accentués
# dans les commentaires

# Pensez à adapter le chemin vers le fichier.
# Ici, il est dans le dossier data présent dans le
# répertoire supérieur
file_handler = open("../data/refGene_hg38.gtf", "r")

# On définit une variable line_number
# qui contiendra le numéro de la ligne courante
line_number = 0

while  line_number < 10:

    # On lit une ligne du fichier avec
    # la méthode readline()
    line =  file_handler.readline()
        # On retire le caractère
        # "\n" à droite. En effet, print produira lui même un
        # caractère "\n".
        line = line.rstrip("\n")
        print(line)
        
        # On ajoute 1 à line_number
        # Sinon la condition 'line_number < 10'
        # sera toujours vérifiée
        line_number = line_number + 1