'''
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting
the respective number of times that the symbols
'A', 'C', 'G', and 'T' occur in s.
'''
import os
path = os.path.abspath("Downloads/rosalind_dna.txt")
with open(path, 'r') as file:
    DNA = file.read()

A = 0
C = 0
G = 0
T = 0
for char in DNA:
    if char == 'A':
        A+=1
    elif char == 'C':
        C+=1
    elif char == 'G':
        G+=1
    elif char == 'T':
        T+=1
print(f'A:{A}')
print(f'C:{C}')
print(f'G:{G}')
print(f'T:{T}')
