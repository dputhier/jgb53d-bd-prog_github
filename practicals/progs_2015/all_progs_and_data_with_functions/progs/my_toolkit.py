# -*- coding: utf8 -*-

"""
    A main program with a argument parser that can be used to start the written programs (head, cut, count, tx_len,...).
"""

import head
import cut
import count
import nb_exons
import tx_len




import argparse


parser = argparse.ArgumentParser(description='A set of tools written during the informatic classes. These tools takes a gtf file as input and perform various tasks.')

parser.add_argument('-i',
                    '--inputfile',
                    type=str,
                    default=None,
                    help="The input file name.")

parser.add_argument('-p',
                    '--program',
                    type=str,
                    choices=["cut", "head", "count", "tx_len", "nb_exons"],
                    default=None,
                    help="The command ")

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


def main_function():

    if args.program == "cut":

        cut.cut(args.inputfile, args.column)

    elif args.program == "head":
    
        head.head(args.inputfile, args.nbline)

    elif args.program == "nb_exons":
    
        nb_exons.nb_exons(args.inputfile)

    elif args.program == "count":
    
        count.count(args.inputfile)
    
    else:
        print("Please choose a program or use '-h' argument for more info.")


if __name__ == "__main__":

    main_function()

