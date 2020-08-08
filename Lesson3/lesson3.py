#读
with open("file") as fh:
    for line in fh:
print (line)

#写
with open ("file", mode="w") as fh:
fh.write()

#同时读写
with open("lesson2.fasta") as file_1, \
        open("output.txt", "w") as file_2:
    file_2.write(file_1.read())

#字典
yilab = {'Rong':'Postdoc','Xiaogang':'Student','Tingshuang':'Teacher'}

# copy of a dict
#In [20]: old_dict = {"a":1, "b":2, "c":3}
#
#In [21]: new_dict = old_list
#
#In [22]: new_dict
#Out[22]: {'a': 1, 'b': 2, 'c': 3}
#
#In [23]: old_dict
#Out[23]: {'a': 1, 'b': 2, 'c': 3}
#
#In [24]: del(old_dict['a'])
#
#In [25]: old_dict
#Out[25]: {'b': 2, 'c': 3}
#
#In [26]: new_dict
#Out[26]: {'b': 2, 'c': 3}

#Also works for sets, need to use .copy() or copy.copy(x)
#In [29]: old_set = set(set(range(9)))
#In [30]: old_set
#Out[30]: {0, 1, 2, 3, 4, 5, 6, 7, 8}
#In [31]: new_set = old_set
#In [32]: new_set.add(9)
#In [33]: old_set
#Out[33]: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#In [34]: new_set
#Out[34]: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#常用函数和方法
del(yilab["Rong"])
yilab.keys()
yilab.values()
yilab.items()

#Hello world
def greet_user():
    """显示简单的问候语"""
    print("Hello")
greet_user()

#传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello!" + username)
greet_user('Xiaogang')

#多参数传递
def greet_user(username, word):
    """显示简单的问候语"""
    print(word + username)
greet_user('Xiaogang', "Hello!")
greet_user(username = 'Xiaogang')

#返回值
def calc_list(input_list):
    """返回一个列表的乘积"""
    mul = 1
    for i in input_list:
        mul *= i
    return mul
calc_list([1,2,3])

#codon
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
