from codon import codon_dict

# print(codon_dict)
# exit()

# os.path.abspath(os.curdir)
# os.chdir('/Users/liuhui/PycharmProjects/python_learn/Lesson3/homework_KEYI')


def reads_fasta(fasta_name):
    """Reads fasta with input name and return a dictionary of name and seq"""
    cds_dict = {}
    with open(fasta_name) as fh:
        for line in fh:
            if line.startswith('>'):
                key = line.strip()
                name_list = key.split()
                key = name_list[0]
                key = key[1:]
            else:
                val = line.rstrip()
                if key not in cds_dict:
                    cds_dict[key] = ''
                cds_dict[key] += val
    return cds_dict
#cds_dict
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
    return(peptide)


#key_test = cds_dict['GU798049.1']
#trans_pro(key_test)

if __name__ == '__main__':
    cds_dict = reads_fasta('../Lesson3/Homework/Home_work.fasta')
    #print(list(cds_dict.keys()))
    # print(list(cds_dict.values()))
    # exit()
    for i in cds_dict:
        pep = trans_pro(cds_dict[i])
        print('>' + i + "\n" + pep)

# pep_dict = cds_dict.copy()
