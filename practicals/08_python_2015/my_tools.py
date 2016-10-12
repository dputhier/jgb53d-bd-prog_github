# -*- coding: utf8 -*-

"""
    Main program with an argument parser that can be used to start the written subprograms (head, cut, count, tx_len,...).
"""

import head
import cut
import count
import nb_exons
import tx_len
import cdna_len



import argparse


parser = argparse.ArgumentParser(description='A set of tools written during the informatic classes. These tools takes a gtf file as input and perform various tasks.')

parser.add_argument('-i',  # La version courte de l'argument.
                    '--inputfile',  # La version longue de l'argument.
                    type=str,       # Le type de l'argument.
                    default=None,   # La valeur par défaut (aucune).
                    help="The input file name.") # L'aide pour cet argument.

parser.add_argument('-p',           # La version courte de l'argument.
                    '--program',    # La version longue de l'argument.
                    type=str,       # Le type de l'argument.
                    choices=["cut", "head", "count", "tx_len", "nb_exons", "cdna_len"], # Les valeurs que l'argument peut prendre.
                    default=None,   # La valeur par défaut (aucune).
                    help="The subprogram to call.") # L'aide pour cet argument.


parser.add_argument('-n',
                    '--nbline',
                    type=int,
                    default=10,
                    help="If the 'head' command is used, the number of line to display")

parser.add_argument('-c',
                    '--column',
                    type=int,
                    default=1,
                    help="If the cut command is used, the column to print (one based) ")


args = parser.parse_args()


def main():

    if args.program == "cut":

        cut.cut(args.inputfile, args.column)

    elif args.program == "head":
    
        head.head(args.inputfile, args.nbline)

    elif args.program == "nb_exons":
    
        nb_exons.nb_exons(args.inputfile)

    elif args.program == "count":
    
        count.count(args.inputfile)

    elif args.program == "cdna_len":
    
        cdna_len.cdna_len_cmd(args.inputfile)

    else:
        print("Please choose a program or use '-h' argument for more info.")


if __name__ == "__main__":

    main()

