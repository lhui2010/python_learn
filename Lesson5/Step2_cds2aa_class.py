from codon import codon_dict


class Cds():
    def __init__(self, sequence):
        self.pep = ""
        self.cds = sequence

    def translate(self):
        """翻译cds生成氨基酸序列"""
        n = 3
        for i in range(0, len(self.cds), n):
            codon = self.cds[i:i + n]
            if codon not in codon_dict:
                self.pep += 'X'
            else:
                self.pep += codon_dict[codon]
        return self.pep


class FastaIO():
    """读取Fasta文件为字典"""

    def __init__(self, fasta_file_name):
        """初始化FastaIO对象并读取fasta文件"""
        self.seq = {}
        self.pep = {}
        with open(fasta_file_name) as fh:
            abc = fh.read()
            fasta_list = abc.split('>')
            fasta_list.pop(0)
            for fasta in fasta_list:
                (name, sequence) = fasta.split('\n', 1)
                self.seq[name] = Cds(sequence.replace('\n', ''))

    def keep_complete(self):
        """
        Only retain fasta with header cotaining complete cds
        eg: GU798049.1 Oryza sativa Japonica Group isolate 27762 ADH1 (adh1) gene, complete cds
        """
        name_list = list(self.seq.keys())
        for k in name_list:
            if 'complete cds' in k:
                pass
            else:
                del self.seq[k]

    def print_pep_by_name(self, gene_name):
        """翻译指定基因名称的cds dict生成氨基酸序列"""
        self.seq[gene_name].translate()
        formated_pep = ">{}\n{}\n".format(gene_name, self.seq[gene_name].pep)
        return formated_pep

    def print_pep(self):
        """打印所有cds dict对应的氨基酸序列"""
        buffer = ""
        for i in self.seq:
            buffer += self.print_pep_by_name(i)
        print(buffer, end ='')


if __name__ == "__main__":
    my_fasta = FastaIO("/Users/liuhui/PycharmProjects/python_learn/Lesson3/homework_KEYI/Homework.fasta")
    my_fasta.keep_complete()
    my_fasta.print_pep()
