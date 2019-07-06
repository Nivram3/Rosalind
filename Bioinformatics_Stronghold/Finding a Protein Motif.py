'''
Title: Finding a Protein Motif
Rosalind ID: MPRT
URL: http://rosalind.info/problems/mprt/

To allow for the presence of its varying forms,
a protein motif is represented by a shorthand as
follows: [XY] means "either X or Y" and {X} means
"any amino acid except X."

For example, the N-glycosylation motif is written as
N{P}[ST]{P}.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation
motif, output its given access ID followed by a list
of locations in the protein string where the motif can
be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

'''


import os
from bs4 import BeautifulSoup
import requests
import re

path = os.path.abspath('Downloads/rosalind_mprt.txt')
with open(path,'r') as file:
    proteins = file.read().split()

# Read AA_seq with Lookahead Assertion Actual Method
for protein in proteins:
    source = requests.get('https://www.uniprot.org/uniprot/' + str(protein) + '.fasta').text
    soup = BeautifulSoup(source, 'lxml')
    find_aa_seq = re.findall(r'[\nA-Z]{10,}', soup.text)
    aa_seq = find_aa_seq[0].replace('\n','')
    pattern = re.compile(r'(?=N[^P][ST]{1}[^P])')
    N_glyco_match = pattern.finditer(aa_seq)
    N_glyco_lst = []
    for match in N_glyco_match:
        N_glyco_lst.append(match.span()[0])
    if len(N_glyco_lst) > 0:
        print(protein)
        for pos in N_glyco_lst:
            print(pos+1, end=' ')
        print()

# Webscrape from Uniprot Table Find "Glycosylation" Method (Did not read from sequence)
for protein in proteins:
    source = requests.get('https://www.uniprot.org/uniprot/' + str(protein)).text
    soup = BeautifulSoup(source, 'lxml')
    try:
        aa_table = soup.find('table', id="aaMod_section")
        aa_positions = aa_table.find_all('td', class_="numeric")
        print(protein)
        position_lst = []
        for position in aa_positions:
            if 'Glycosylation' in str(position):
                position_lst.append(position.text)  # end = ' ' works but last space leads to an incorrect submission
        print(" ".join(pos for pos in position_lst))
    except AttributeError:  # if None then just print protein
        pass
