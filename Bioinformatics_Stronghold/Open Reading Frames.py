#!/usr/bin/env python

'''
Title: Open Reading Frames
Rosalind ID: ORF
URL: http://rosalind.info/problems/orf/

A given DNA string has six total reading frames since
either strand of the DNA double helix can act as the
coding strand. RNA will have same sequence as coding
strand except for the replacement of T with U.

Open reading frame is from the start to the stop codon
without other stop codons inbetween.

Given: A DNA string  of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that
can be translated from ORFs of. Strings can be
returned in any order.
'''
import re
import os
path = os.path.abspath('Downloads/rosalind_orf.txt')
with open(path,'r') as file:
    FASTA_file = re.finditer(r'[ACGT]+',file.read())
    FASTA_string =''
    for string in FASTA_file:
        FASTA_string += string[0]

DNA_amino_converter = {
    'TTT': 'F', 'TTC': 'F',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y',
    'TAA': '%', 'TAG': '%',
    'CAT': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C',
    'TGA': '%', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}
all_open_reading_frames = set()
def open_reading_frame(codon_list):
    amino_seq = ''
    for codon in codon_list:
        try:
            amino_seq += DNA_amino_converter.get(codon)
        except:
            continue
    final_seq_matches = re.findall(r'(?=(M[A-Z]*%))',amino_seq)
    for match in final_seq_matches:
        all_open_reading_frames.add(match.strip('%'))

def find_reading_frames(my_string, start_index):
    codons = [my_string[i:i+3] for i in range(start_index, len(my_string), 3)]
    return open_reading_frame(codons)

def rev_reading_frame(my_string):
    rev = ''
    for char in my_string:
        if char == 'A':
            rev += 'T'
        elif char == 'C':
            rev += 'G'
        elif char == 'G':
            rev += 'C'
        else:
            rev += 'A'
    return rev
for num in range(0,3):
    find_reading_frames(FASTA_string, num)
    # other reading frame must be reversed
    # and have nucleotide bases switched for correct
    # reading in 3' to 5' direction
    find_reading_frames(rev_reading_frame(FASTA_string[::-1]), num)

for aa_seq in all_open_reading_frames:
    print(aa_seq)