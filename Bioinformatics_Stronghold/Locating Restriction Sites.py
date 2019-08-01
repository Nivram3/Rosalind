'''
Title: Locating Restriction Sites
Rosalind ID: revp
URL: http://rosalind.info/problems/revp/

Reverse palindrome: DNA string is equal to its
reverse complement.
Palindrome is read same forward and back.
GCATGC is a reverse palindrome because its reverse
complement is GCATGC.

Example:
DNA String: GCATGC
Complement: CGTACG
Reverse Complement: GCATCG

Counterexample:
DNA String: TCAAT
Complement: AGTTA
Reverse Complement: ATTGA
'''
import os
import re

file_name = "rosalind_revp.txt"
for root, dirs, files in os.walk(r'C:\Users'):
    for name in files:
        if name == file_name:
            path = os.path.join(root, name)

with open(path, 'r') as file:
    FASTA_format_string = file.read()

my_DNA_string = re.findall(r'[CGAT\s]+', FASTA_format_string)
my_DNA_string = my_DNA_string[0].replace('\n', '')
print(my_DNA_string)
def rev_pali(my_str):
    my_complement = ''
    for char in my_str:
        if char == 'A':
            my_complement += 'T'
        elif char == 'C':
            my_complement += 'G'
        elif char == 'G':
            my_complement += 'C'
        else:
            my_complement += 'A'
    my_rev_complement = ''.join(reversed(my_complement))
    if my_rev_complement == my_str:
        # print(my_rev_complement)
        return True
    else:
        return False

for length in range(4, 13):
    for position in range(0,len(my_DNA_string)-length+1):
        if rev_pali(my_DNA_string[position:position+length]) is True:
            print(position+1, length)

'''
Interesting reverse complement function:
    essentially make a translation table and translate
    the string but return it by iterating in -1 step size 
    return(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))
'''