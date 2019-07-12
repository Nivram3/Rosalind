'''

Title: Inferring mRNA from Protein
Rosalind ID: MRNA
URL: http://rosalind.info/problems/mrna/

Modular arithmetic:
Divide both 14 and 23 by 3, the remainder is 2 in both cases.
In Python 14%3 = 2 --> (3 x 4) + 2 = 14
Means 14 is congruent to 23 modulo 3.
a ≅ b mod n
c ≅ d mod n
then a + c ≅ b + d mod n
then a - c ≅ b - d mod n
then a x c ≅ b x d mod n

Some Rosalind problems will ask for a (very large)
integer solution modulo a smaller number to avoid
the computational pitfalls that arise with storing
such large numbers.

Given: A protein string of length at most 1000 aa (amino acids).

Return: The total number of different RNA strings
from which the protein could have been translated,
modulo 1,000,000. (Don't neglect the importance of
the stop codon in protein translation.)

Sample: MA

Output: 12%1,000,000 = 12
- M (one possible mRNA combination)
- A (4 possible mRNA combinations)
- STOP (3 possible combinations)
'''
import os
path = os.path.abspath('Downloads/rosalind_mrna.txt')
with open(path,'r') as file:
    protein = str(file.read()).strip('\n')
aa_dict = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4,
    'H': 2, 'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4,
    'W': 1, 'Y': 2, 'STOP': 3,
}
tot_combo = 1
for amino_acid in protein:
    tot_combo *= aa_dict.get(amino_acid)
print((tot_combo*aa_dict.get('STOP'))%1000000)
