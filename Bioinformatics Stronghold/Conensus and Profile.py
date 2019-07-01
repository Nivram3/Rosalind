import os
import re

path = os.path.abspath('Downloads/rosalind_cons.txt')

with open(path,'r') as f:
    DNA_strings = f.read()
matches = re.findall(r'[ACGT\n]+',DNA_strings)
DNA_strings_revised = []
print('DNA STRINGS')
for match in matches:
    for char in match:
        char = char.replace('\n',' ')
    match = ''.join(match.splitlines())
    DNA_strings_revised.append(match)
    match = ' '.join(match)
    print('\t' + match)

consensus = ''
print('Profile Matrix')
print('A: ',end=' ')
i = 0
while i < len(DNA_strings_revised[0]):
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for string in DNA_strings_revised:
        if string[i] == 'A':
            A_count +=1
        if string[i] == 'C':
            C_count +=1
        if string[i] == 'G':
            G_count +=1
        if string[i] == 'T':
            T_count +=1
    max_base = []
    max_base.extend([A_count,C_count,G_count,T_count])
    max_index = max_base.index(max(max_base))
    if max_index == 0:
        consensus = consensus + 'A '
    elif max_index == 1:
        consensus = consensus + 'C '
    elif max_index == 2:
        consensus = consensus + 'G '
    elif max_index == 3:
        consensus = consensus + 'T '
    else:
        print('Error')
    print(A_count, end = ' ')
    i+=1

print('\nC: ',end=' ')
i = 0
while i < len(DNA_strings_revised[0]):
    C_count = 0
    for string in DNA_strings_revised:
        if string[i] == 'C':
            C_count +=1
    print(C_count, end = ' ')
    i+=1
print('\nG: ',end=' ')
i = 0
while i < len(DNA_strings_revised[0]):
    G_count = 0
    for string in DNA_strings_revised:
        if string[i] == 'G':
            G_count +=1
    print(G_count, end = ' ')
    i+=1
print('\nT: ',end=' ')
i = 0
while i < len(DNA_strings_revised[0]):
    T_count = 0
    for string in DNA_strings_revised:
        if string[i] == 'T':
            T_count +=1
    print(T_count, end = ' ')
    i+=1

print('\nConsensus\n\t'+ consensus)
print(consensus.replace(' ',''))
'''
A matrix is a rectangular table of values divided 
into rows and columns. An m x n matrix has m rows and
n columns. 
Given a matrix A, we write A i,j to indicate the value found at the 
intersection of row i and column j.

Profile Matrix: 
A matrix encoding the number of times that each symbol 
of an alphabet occurs in each position from a 
collection of strings.

DNA strings in a matrix all the same length 
Profile shape will be 4(num of dif bases) x length 

Profile 1,j is the num of times A is in jth column 

Consensus String (c): 
Formed from a collection of strings by taking the most
common symbol appearing at each position of the strings 
(see the table below). When constructed over a 
collection of genetic strings, the consensus string 
represents an average case organism over the collection.

DNA Strings:
    A T C C A G C T
    G G G C A A C T
    A T G G A T C T
    A A G C A A C C
    T T G G A A C T
    A T G C C A T T
    A T G G C A C T
Profile:
A   5 1 0 0 5 5 0 0
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6
Consensus:	
    A T G C A A C T 
'''