'''
Sequence motifs are short, recurring patterns in DNA
that are presumed to have a biological function.
Often they indicate sequence-specific binding sites
for proteins such as nucleases and transcription
factors (TF).

Given two strings s and t, t is a substring of s if t
is contained as a contiguous collection of symbols in
s (as a result, t must be no longer than s).

Position of symbol: total num of symbols to its left
including itself. eg. AUG, position of U is 2

location of substring is its beginning position in
the larger string

Given: Two DNA strings s and t

Return: All locations of t as a substring of s.

INPUT: GATATATGCATATACTT and ATAT
OUTPUT: 2 4 10
'''
import re
import os
path = os.path.abspath('Downloads/rosalind_subs.txt')
with open(path,'r') as f:
    my_strings = (f.read()).split('\n')

s = my_strings[0]
t = my_strings[1]

#can't + t after, use % interpolation
matches = re.finditer(r'(?=%s)'%(t),s)
for match in matches:
    print(match.start()+1,end=' ')

