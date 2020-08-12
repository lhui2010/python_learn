import os,sys
"""os.getcwd()
path = '/Users/zhangrong/PycharmProjects/python_learn/python.lesson4/homework'
os.chdir(path)
retval = os.getcwd()
print("当前工作目录为 %s" % retval)
lsfile = os.listdir(path)
for file in lsfile:
    print(file)
"""
#convert interleaving fas to non-interleave
with open('complete.fasta') as fas_interleave, open("fas2line.fas", "w") as fas_2line:
    fas_seq = []
    for line in fas_interleave:
        if line.startswith(">"):
            if fas_seq:
                fas_2line.write("".join(fas_seq)+"\n")
                fas_seq=[]
            fas_2line.write(line)
        else:
            fas_seq.append(line.strip())
    if fas_seq:
        fas_2line.write("".join(fas_seq)+"\n")

#add module codon
print(sys.path)
#sys.path.append(path)
from codon import codon_dict
print(codon_dict["ACT"])

#convert fas to dictionary
nt2aa_fin = open("nt2aa_fin.fas", "w")
fas_dict = {}
seq_name = ""
sequence = ""
fas_2line = open("fas2line.fas")
for line_dict in fas_2line:
    if line_dict.startswith(">"):
        seq_name = line_dict.strip("\n")
    else:
        sequence = line_dict.strip("\n")
    fas_dict[seq_name]=sequence
nt2aa_fin.write(str(fas_dict))

#convert nt to aa
def nt2aa(input_seq):
    pep_seq=""
    a = len(input_seq)%3
    if a == 0:
        for i in range(0,len(input_seq),3):
            if "N" in input_seq[i:i+3]:
                pep_seq = "X"
            else:
                pep_seq+=codon_dict[input_seq[i:i+3]]
        return pep_seq
    else:
        for i in range(0,(len(input_seq)-a),3):
            if "N" in input_seq[i:i+3]:
                pep_seq = "X"
            else:
                pep_seq+=codon_dict[input_seq[i:i+3]]
        return pep_seq

fasta_aa = {}
for x,y in fas_dict.items():
#    fas_dict[x] = nt2aa("".join(y))
    for l in range(0,len(y)):
        if y[l] not in ["A","T","C","G","N"]:
            y.replace([l], 'N')

    aa = nt2aa(y)
    fasta_aa[x] = aa

print(fasta_aa)
#input_seq = y_new
#pep_seq = nt2aa(y)
#nt2aa_fin2 = open("nt2aa_fin2.fas", "w")
#nt2aa_fin2.write(pep_seq)

