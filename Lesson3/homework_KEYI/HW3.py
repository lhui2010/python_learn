codon_dict = {
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',                               # Alanine
    'TGC': 'C', 'TGT': 'C',                                                           # Cysteine
    'GAC': 'D', 'GAT': 'D',                                                           # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',                                                           # Glutamic Acid
    'TTC': 'F', 'TTT': 'F',                                                           # Phenylalanine
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',                               # Glycine
    'CAC': 'H', 'CAT': 'H',                                                           # Histidine
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I',                                             # Isoleucine
    'AAA': 'K', 'AAG': 'K',                                                           # Lysine
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'TTA': 'L', 'TTG': 'L',   # Leucine
    'ATG': 'M',                                                                         # Methionine
    'AAC': 'N', 'AAT': 'N',                                                           # Asparagine
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',                               # Proline
    'CAA': 'Q', 'CAG': 'Q',                                                           # Glutamine
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 'AGA': 'R', 'AGG': 'R',   # Arginine
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'AGC': 'S', 'AGT': 'S',   # Serine
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',                               # Threonine
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',                               # Valine
    'TGG': 'W',                                                                         # Tryptophan
    'TAC': 'Y', 'TAT': 'Y',                                                           # Tyrosine
    'TAA': 'U', 'TAG': 'U', 'TGA': 'U'                                              # Stop
    }

import os
os.path.abspath(os.curdir)
os.chdir('/Users/liuhui/PycharmProjects/python_learn/Lesson3/homework_KEYI')

# read text and make cds into a dictionary
flag = 0
cds_dict = {}
with open ('Home_work.fasta') as fh:
    for line in fh:
        if line.startswith('>'):
            if 'complete cds' in line:
                key = line.strip()
                name_list = key.split()
                key = name_list[0]
                key = key[1:]
                flag = 1
            else:
                flag = 0
        else:
            if flag == 1:
                val = line.rstrip()
                if key not in cds_dict:
                    cds_dict[key] = ''
                cds_dict[key] += val
cds_dict
# help(line)

# split string into codons and translate them

def trans_pro(input_key):
    """翻译cds生成氨基酸序列"""
    n = 3
    peptide = ""
    for i in range(0, len(input_key), n):
        codon = input_key[i:i + n]
        if codon not in codon_dict:
            peptide += 'X'
        else:
            peptide += codon_dict[codon]
    print(peptide)


key_test = cds_dict['GU798049.1']
trans_pro(key_test)

# pep_dict = cds_dict.copy()
