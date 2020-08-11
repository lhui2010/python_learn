import argparse
from Step2_cds2aa_class import FastaIO




if __name__ == "__main__":
    #my_fasta = FastaIO("/Users/liuhui/PycharmProjects/python_learn/Lesson3/homework_KEYI/Homework.fasta")
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
    my_fasta = FastaIO(input_file_name)
    my_fasta.print_pep()
