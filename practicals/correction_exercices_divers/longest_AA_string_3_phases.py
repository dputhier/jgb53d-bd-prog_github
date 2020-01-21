## This code will search for the longuest ORF in the 3 phases.
## Note that we won't test here for reverse-complemented sequences.

input_file ="cdna_seq.fa_short.txt"
file_handler = open(input_file, "r")

table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
}


for line in file_handler:
    line = line.replace("\n", "")

    if line.startswith(">"):
        header = line
    else:
        longuest_protein = ""

        if len(line) < 3:
            longuest_protein = ""

        for frame in [0, 1, 2]:
            for i in range(frame, len(line), 3):
                codon = line[i:i+3]
                if codon == 'ATG':
                    protein = "M"
                    for j in range(i+3, len(line), 3):
                        codon = line[j:j+3]
                        if len(codon) == 3:
                            protein += table[codon.upper()]
                            if codon in ['TAA', 'TAG', 'TGA']:
                                if len(protein)  > len(longuest_protein):
                                    longuest_protein = protein
                                break
        print(header)
        print(longuest_protein)
