'''
A common substring of a collection of strings is a
substring of every member of the collection.
We say that a common substring is a longest common
substring if there does not exist a longer common
substring.

the longest common substring is not necessarily unique;
for a simple example, "AA" and "CC" are both longest
common substrings of "AACC" and "CCAA".

Given: a collection of DNA Strings in FASTA format
Return: longest common substring of collection
(if multiple, return any single solution)
'''

import os
import re
path = os.path.abspath('Downloads/rosalind_lcsm.txt')
with open(path,'r') as file:
    strings = file.read()
string_names = re.findall(r'>Rosalind_\d+',strings)
o_string_sqnces = re.findall(r'[GATC\n]+',strings)
string_sqnces = []
for match in o_string_sqnces:
    string_sqnces.append(match.replace('\n',''))


# while True:
#     if string_sqnces[0][index:(index+length)] in string_sqnces:
#         print('match for:',string_sqnces[0][index:(index + length)])
#         memory = string_sqnces[0][index:(index+length)]
#         length+=1
#     else:
#         print('no match for:',string_sqnces[0][index:(index+length)])
#         index += 1
#         if len(string_sqnces[0][index:(index+length)]) <= len(memory):
#             print('final:',memory)
#             break

# while True:
#     matching = 0
#     print(A[index:(index + length)])
#     for string in string_sqnces:
#         if A[index:(index + length)] in string:
#             matching+=1
#             idx = string_sqnces.index(string)
#             print(string_names[idx],end=' ')
#     print('\n',matching)
#     if matching == len(string_sqnces):
#         print('match for:',A[index:(index + length)],'\n')
#         memory = A[index:(index+length)]
#         length+=1
#     else:
#         print('no match for:',A[index:(index+length)],'\n')
#         index += 1
#         if len(A[index:(index+length)]) <= len(memory):
#             print('final:',memory)
#             break

index = 0
length = 1
memory = ''
A = string_sqnces[0]

while True:
    print(A[index:(index + length)])
    matching = sum(A[index:(index + length)] in s for s in string_sqnces)
    print('Matches:', matching)
    if matching == len(string_sqnces):
        print('100% match for:',A[index:(index + length)],'\n')
        memory = A[index:(index + length)]
        length += 1
    else:
        print('not 100% match for:',A[index:(index+length)],'\n')
        index += 1
        if len(A[index:(index+length)]) < len(memory):
            print('final:',memory,'\n')
            break
