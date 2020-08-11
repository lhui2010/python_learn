# 产生一个f2.fasta的文件（多行）
   ...: f2 = open("f2.fasta","w")
   ...: f1 = open('home-work.fasta','r').readlines()
   ...: for line in f1:
   ...:     if line.startswith('>'):
   ...:         f2.write('\n' + line)
   ...:     if not line.startswith('>'):
   ...:         f2.write(line.strip("\n") ) #把file_1里面的文本读进去，并把换行符去掉
   ...: print(f2)
##把id提出来
        f2 = open("f2.fasta","r").readlines()
   ...: f3 = open("f3.fasta","w")
   ...: for line in f2:
   ...:     if line.startswith('>'):
   ...:         f3.write(line.split()[0])
   ...: print(f3)

#####存入字典,d = dict(zip(li1,li2))