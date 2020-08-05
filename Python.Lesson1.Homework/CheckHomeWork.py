#!/usr/bin/env python

import argparse
import textwrap

def main():
    prog_name = "Lesson1 Homework Checker"
    usage = """
    Copy your own calculation into a text with fasta format with a specified 
    name (wk1.1.output.txt for this example):
        >sh4
        ATGTCGGGC..
    Use the following script to check your result.
    python CheckHomeWork.py --homework 1 wk1.1.output.txt
    python CheckHomeWork.py --homework 2 wk1.2.output.txt
    """

    homework_list = ["","ATGTCGGGCTCCTCTGCCGACCCCTCGCCATCCGCCTCGACCGCGGGGGCGGCGGTCTCGCCGCTCGCGCTGCTCCGCGCGCACGGCCACGGCCACGGGCACCTGACTGCTACGCCGCCGTCGGGGGCGACGGGGCCGGCGCCGCCGCCGCCGTCGCCGGCGTCGGGGTCGGCGCCGCGGGACTACCGCAAGGGGAACTGGACGCTGCACGAGACGCTCATCCTCATCACCGCCAATCGTCTGGACGACGACCGCCGCGCCGGCGTTGGGGGCGCGGCGGCTGGTGGCGGCGGCGCCGGGTCGCCGCCGACGCCGAGGTCGGCGGAGCAGCGGTGGAAGTGGGTGGAGAACTACTGCTGGAAGAACGGCTGCCTCCGCAGCCAGAACCAGTGCAATGACAAGTGGGACAACCTCCTCCGCGACTACAAGAAGGTCCGCGACTACGAGTCCCGCGTCGCCGCCGCCGCCGCCACCGGCGGCGCGGCCGCCGCCAACTCCGCCCCCCTCCCGTCGTACTGGACGATGGAGCGGCACGAGCGCAAGGACTGCAACCTCCCCACCAACCTGGCGCCGGAGGTCTACGACGCGCTCTCCGAGGTGCTCTCCCGCCGCGCGGCGCGACGCGGCGGCGCCACGATCGCGCCCACCCCGCCGCCACCACCGCTCGCGCTGCCGCTGCCGCCGCCGCCGCCGCCCTCGCCGCCGAAGCCTCTCGTCGCGCAGCAGCAGCACCACCATCACGGCCATCACCACCACCCACCTCCTCCTCAGCCGCCGCCGTCGTCGCTGCAGCTCCCTCCGGCGGTCGTGGCTCCGCCGCCGGCGTCCGTTTCCGCGGAGGAGGAGATGTCGGGGTCGTCGGAGTCGGGGGAGGAGGAGGAGGGGTCGGGCGGGGAGCCGGAGGCGAAGCGGCGGCGGCTGAGCCGGCTGGGGTCGAGCGTGGTGAGGAGCGCGACGGTGGTGGCGAGGACGCTGGTGGCGTGCGAGGAGAAGCGGGAGCGCCGGCACCGGGAGCTGCTGCAGCTGGAGGAGCGGCGGCTGCGCCTCGAGGAGGAGCGCACCGAGGTCCGCCGCCAGGGCTTCGCCGGCCTCATCGCCGCCGTCAACAGCCTCTCCTCCGCCATCCACGCCCTCGTCTCCGACCACCGCAGCGGCGACTCCTCCGGCCGATGA",
                     "tcaggtctgtcacatgagaagagagcgaagtagctcagctcagcccccactcgctcacatggaacgcctctgctcgcctcgactacttaaccagctaaacgctcggttgattaggagaggaaaaaaaacgagggaaaaaacgggtggaaacacacgcaaaaacacaacgccgtgcggccttgtaaatacgggcgacgccgacgcgcatcgctccccgaacaccaaacgcctcagcttgccttggctctcgccagtcgctacgcccgcgacgacacgaccgcgccgcgcgcgcgcgagcgagcgagcATGTCGGGCTCCTCTGCCGACCCCTCGCCATCCGCCTCGACCGCGGGGGCGGCGGTCTCGCCGCTCGCGCTGCTCCGCGCGCACGGCCACGGCCACGGGCACCTGACTGCTACGCCGCCGTCGGGGGCGACGGGGCCGGCGCCGCCGCCGCCGTCGCCGGCGTCGGGGTCGGCGCCGCGGGACTACCGCAAGGGGAACTGGACGCTGCACGAGACGCTCATCCTCATCACCGCCAATCGTCTGGACGACGACCGCCGCGCCGGCGTTGGGGGCGCGGCGGCTGGTGGCGGCGGCGCCGGGTCGCCGCCGACGCCGAGGTCGGCGGAGCAGCGGTGGAAGTGGGTGGAGAACTACTGCTGGAAGAACGGCTGCCTCCGCAGCCAGAACCAGTGCAATGACAAGTGGGACAACCTCCTCCGCGACTACAAGAAGGTCCGCGACTACGAGTCCCGCGTCGCCGCCGCCGCCGCCACCGGCGGCGCGGCCGCCGCCAACTCCGCCCCCCTCCCGTCGTACTGGACGATGGAGCGGCACGAGCGCAAGGACTGCAACCTCCCCACCAACCTGGCGCCGGAGGTCTACGACGCGCTCTCCGAGGTGCTCTCCCGCCGCGCGGCGCGACGCGGCGGCGCCACGATCGCGCCCACCCCGCCGCCACCACCGCTCGCGCTGCCGCTGCCGCCGCCGCCGCCGCCCTCGCCGCCGAAGCCTCTCGTCGCGCAGCAGCAGCACCACCATCACGGCCATCACCACCACCCACCTCCTCCTCAGCCGCCGCCGTCGTCGCTGCAGCTCCCTCCGGCGGTCGTGGCTCCGCCGCCGGCGTCCGTTTCCGgtaatggtcggtgcgcgcaccgtacacttaatactcatagtagctgttacatcccctcccctccaaaccatttactactgttctctcacactgatatgtgggcccacctcgcagcgagctgagctccgccactatacgttattaaaagcccgcgttatgattgggctagttacgttgttgagttgagctggtcgtaattatttactaccgctacattttttttacctttttaccgtggggttcgggagagggtggtcgcggtaataataatgtcctcaactcaggggttgggagaataaagctgcgtgcagtgtggtgcagttcatgcatgggaaaggtgatgcgaatccggatattttatgggggtttaattgaaagatttactccacgacgatactaccctctactcctgccatgctgcaagcatgcgtaatgcgttacattgcgaaatcactcgctttgaatgaaaaaaaagcctgaaactttggagaaaaaaaaagcaccttttgttttctcctcgtgcatgcatgccgcgctgcgtatcttgaactactttggacttttgtatcgatcaacaaaactatacctatattagcagtaattaatactacatttgtagatatcctttgaccgttctatcttatttttgataattaaaaaaattagttacatttaaaaatgctatttatattttattatctaataacaataagtgtattagttaaatattaaacgttggatatgaatagtttaaaacgttggatatgaatagtttaaaactgtattgttttggggcggagtgagtaattgattgatcgattaattaagtggttgactaatgtgtgtgtgatttatttgtgtagCGGAGGAGGAGATGTCGGGGTCGTCGGAGTCGGGGGAGGAGGAGGAGGGGTCGGGCGGGGAGCCGGAGGCGAAGCGGCGGCGGCTGAGCCGGCTGGGGTCGAGCGTGGTGAGGAGCGCGACGGTGGTGGCGAGGACGCTGGTGGCGTGCGAGGAGAAGCGGGAGCGCCGGCACCGGGAGCTGCTGCAGCTGGAGGAGCGGCGGCTGCGCCTCGAGGAGGAGCGCACCGAGGTCCGCCGCCAGGGCTTCGCCGGCCTCATCGCCGCCGTCAACAGCCTCTCCTCCGCCATCCACGCCCTCGTCTCCGACCACCGCAGCGGCGACTCCTCCGGCCGATGAtcgccattgcaatcatatgcaatgcagcaaggacgatcgatgtaaataacccatggagatgcatggatcgaggcatcggattattgtttggaatggctgcaagaagaggagtagctatatatttttttttttgagtgtgcatcgccatcgcgtcgtctgcgagtattgggagtacggtgcattgcatgcacaacgcctccgtttcttgatttctttctttctctcctgtgtcctgtgatttttttgttgtttattcttttcgtgcaattagtggagagactggcaggtgtgtggtgtgaatgatcgaaatggttagtgtggctgctgctgc"]

    parser = argparse.ArgumentParser(
        prog=prog_name,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(usage),
        epilog="")
    parser.add_argument("qry1", help="qry1 file")
    parser.add_argument("-w", "--homework", default=1, type=int, help="Select homework, 1 or 2")
    args = parser.parse_args()

    qry1_file = args.qry1
    home_work_id = int(args.homework)
    flag=0
    qry_seq = ""
    with open(qry1_file) as fh:
        for line in fh:
            if line.startswith(">"):
                flag=1
            elif flag and line.strip() != "":
                qry_seq += line.rstrip()
    if homework_list[home_work_id] == qry_seq:
        print("Your answer is correct")
    else:
        print("Oops! Looks something went wrong")

if __name__ == "__main__":
    main()
