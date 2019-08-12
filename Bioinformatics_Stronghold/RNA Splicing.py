#!usr/bin/python
'''
Title: RNA Splicing
Rosalind ID: splc
URL: http://rosalind.info/problems/splc/

Background:
1. RNA Polymerase breaks H+ bonds between complementary
bases in DNA and creates pre-mRNA by moving down one
of the DNA strands (template) and adds the complementary
base (where uracil is used in place of thymine).
2. As RNAP's move along, their transcription bubble
shifts too and already passed sections of DNA zip
back together.
3. Pre-mRNA is made of many chopped segments of introns
and exons. Exons are used to create the mRNA for translation.
The process of getting rid of introns and including only
exons is called splicing and is done by a spliceosome.

Given:
A DNA string and a collection of intron substrings
Return:
A protein string from only translation of the exons
'''
from Bio import SeqIO
from Bio.Seq import Seq
import os

file_name = "rosalind_splc.txt"
for root, dirs, files in os.walk(r'C:\Users'):
    for name in files:
        if name == file_name:
            path = os.path.join(root, name)

# with open(path, "r") as handle:
#     for record in SeqIO.parse(handle, "fasta"):
#         print(record.id)

records = list(SeqIO.parse(path, 'fasta'))
my_DNA_string = records[0].seq
my_Introns = records[1:]
print(my_DNA_string)
for intron in my_Introns:
    if str(intron.seq) in my_DNA_string:
        my_DNA_string = str(my_DNA_string).replace(str(intron.seq),'')
print(my_DNA_string)

print("Protein:",Seq(my_DNA_string).translate())
