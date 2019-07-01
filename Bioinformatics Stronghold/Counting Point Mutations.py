'''
Given two strings of equal length,
The Hamming distance between each string is the
number of symbols in the string that do not match up

The Hamming distance between two strings having the
same length is the minimum number of symbol
substitutions required to transform one string into
the other.

s1 and s2, distance dH (s1, s2)

Given two DNA strings of equal length
Return the Hamming Distance
'''

import os
path = os.path.abspath('Downloads/rosalind_hamm.txt')
with open(path,'r') as file:
    my_strings = file.read()
my_strings = my_strings.split('\n')
print(my_strings)
s1 = my_strings[0]
s2 = my_strings[1]

i = 0
hamming_distance = 0
while i < len(s1):
    if s1[i] == s2[i]:
        i+=1
        continue
        print('a') # only shows up if pass written not continue
    else:
        i+=1
        hamming_distance+=1
print(hamming_distance)