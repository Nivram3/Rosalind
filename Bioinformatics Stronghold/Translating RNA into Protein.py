'''
20 amino acids in proteins use 20 letters of the alphabet

RNA Codon Table of RNA to amino acids

UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G

Given an mRNA sting, convert to a protein string
'''

import os
path = os.path.abspath('Downloads/rosalind_prot.txt')

with open(path,'r') as f:
    RNA = f.read()
codons = {'UUU':'F',
          'CUU':'L',
          'AUU':'I',
          'GUU':'V',
          'UUC':'F',
          'CUC':'L',
          'AUC':'I',
          'GUC':'V',
          'UUA':'L',
          'CUA':'L',
          'AUA':'I',
          'GUA':'V',
          'UUG':'L',
          'CUG':'L',
          'AUG':'M',
          'GUG':'V',
          'UCU':'S',
          'CCU':'P',
          'ACU':'T',
          'GCU':'A',
          'UCC':'S',
          'CCC':'P',
          'ACC':'T',
          'GCC':'A',
          'UCA':'S',
          'CCA':'P',
          'ACA':'T',
          'GCA':'A',
          'UCG':'S',
          'CCG':'P',
          'ACG':'T',
          'GCG':'A',
          'UAU':'Y',
          'CAU':'H',      'AAU':'N',      'GAU':'D',
          'UAC':'Y',     'CAC':'H',      'AAC':'N',      'GAC':'D',
          'UAA':'',   'CAA':'Q',      'AAA':'K',      'GAA':'E',
          'UAG':'',   'CAG':'Q',      'AAG':'K',      'GAG':'E',
          'UGU':'C',      'CGU':'R',      'AGU':'S',      'GGU':'G',
          'UGC':'C',      'CGC':'R',      'AGC':'S',      'GGC':'G',
          'UGA':'',   'CGA':'R',      'AGA':'R',      'GGA':'G',
          'UGG':'W',      'CGG':'R',      'AGG':'R',      'GGG':'G',}
print(RNA)
def RNA_Protein(string,*args):
    amino = ''
    for arg in args:
        try:
            amino = amino + string[arg]
        except IndexError:
            print('...',end='')
    print(codons.get(amino),end='')

i = 0
while i < len(RNA):
    index_triplet = tuple(range(i,i+3))
    RNA_Protein(RNA,*index_triplet)
    i+=3

'''
string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]]

print decoded'''