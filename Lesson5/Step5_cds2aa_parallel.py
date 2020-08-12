import argparse

from Step2_cds2aa_class import FastaIO
from multiprocessing import Pool


class FastaIOParallel(FastaIO):
    def __init__(self, fasta_file_name):
        super().__init__(fasta_file_name)

    def print_pep_parallel(self, threads=2):
        """翻译cds dict生成氨基酸序列"""
        self.print = ""
        with Pool(threads) as p:
            result = p.map(self.get_pep_fasta_by_name, self.seq.keys())
        print("".join(result), end="")


if __name__ == "__main__":
    # my_fasta = FastaIO("/Users/liuhui/PycharmProjects/python_learn/Lesson3/homework_KEYI/Homework.fasta")
    # #https://www.slideshare.net/tisto/argparse-python-command-line-parser
    parser = argparse.ArgumentParser(
        description="Translate cds to pep"
    )
    #parser.print_help()
    # add positional arguments
    parser.add_argument('input', help="Input file of cds")
    # reads from sys.argv and extract args
    args = parser.parse_args()

    input_file_name = args.input
    my_fasta = FastaIOParallel(input_file_name)
    my_fasta.print_pep_parallel()
