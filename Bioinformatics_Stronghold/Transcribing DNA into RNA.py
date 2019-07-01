import os
path = os.path.abspath("Downloads/rosalind_rna.txt")
with open(path, 'r') as file:
    DNA = file.read()

RNA = DNA.replace('T','U')
print(DNA)
print(RNA)