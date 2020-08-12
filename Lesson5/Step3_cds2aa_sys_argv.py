import sys
sys.path.append("/Users/liuhui/PycharmProjects/python_learn/Lesson5")
from Step2_cds2aa_class import FastaIO

if __name__ == "__main__":
    #my_fasta = FastaIO("/Users/liuhui/PycharmProjects/python_learn/Lesson3/homework_KEYI/Homework.fasta")
    input_file_name = sys.argv[1]
    my_fasta = FastaIO(input_file_name)
    my_fasta.print_pep()
