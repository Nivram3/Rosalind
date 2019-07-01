'''
GC-content of DNA is given by % of nucleotides bases
that are C or G. Note: (reverse also has same %)

FATSA: common string labelling method
In this format, the string is introduced by a line
that begins with '>', followed by some labeling
information.
Subsequent lines contain the string itself; the first
line to begin with '>' indicates the label of the next
string.

eg.

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCG
GCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCC
GAAGGTCTATATCCATTTGTCAGCAGACACGC

Given: At most 10 DNA strings in FASTA format (
of length at most 1 kbp each).

Return: The ID of the string having the highest
GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see
the note on absolute error below.
'''
import re
import os
path = os.path.abspath('Downloads/rosalind_gc.txt')
with open(path, 'r') as f:
    raw_Info = f.read()

DNA_ID = re.findall(r'Rosalind_\d{4}',raw_Info)
DNA_Strings = re.findall(r'[AGCT\s]+',raw_Info)

def GC_content(DNA:str)-> str:
    DNA = DNA.replace('\n','')
    G_count = DNA.count('G')
    C_count = DNA.count('C')
    return (G_count + C_count)/len(DNA)
highest_GC_percent = 0
for string in DNA_Strings:
    # must be within 0.001 of correct answer
    if round(GC_content(string),7)*100 > highest_GC_percent:
        highest_GC_percent = round(GC_content(string),7)*100
        highest_GC_string = string
print(highest_GC_string)
print(DNA_ID[DNA_Strings.index(highest_GC_string)])
print(highest_GC_percent)

# submission
# I finally solve this problem after trying 7 times.
# Put your answer on the same line with a space
# between the id and the percent like this:
# Rosalind_6106 53.273138%
# Don't put ">" before the id and don't miss "%" at
# the end