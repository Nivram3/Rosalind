'''
In DNA strings, symbols 'A' and 'T' are complements
of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the
string sc formed by reversing the symbols of s,
then taking the complement of each symbol
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

# replace letters then reverse string or vice versa

import os
path = os.path.abspath("Downloads/rosalind_revc.txt")
with open(path, 'r') as file:
    DNA = file.read()


# num = 1000, time = 0.0186, 0.0228, 0.0294, 0.0304, 0.0199
DNA = list(DNA)
DNA.remove('\n') # removes first matching value
# pop removes the item at a specific index and returns it.
# lst = [3, 2, 2, 1]
# >>> del lst[1:] --> [3]
DNA.reverse()

for index,char in enumerate(DNA):
    if char == 'G':
        DNA[index] = 'C'
    elif char == 'C':
        DNA[index] = 'G'
    elif char == 'A':
        DNA[index] = 'T'
    elif char == 'T':
        DNA[index] = 'A'
    else:
        continue
        # pass does nothing, continue goes to next iteration
        # difference shown if there is a statement after the if statement
compliment = DNA
print(compliment)
comp_string = ''
print(comp_string.join(compliment))
