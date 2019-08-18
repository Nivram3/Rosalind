'''
Title: Enumerating k-mers Lexicographically
Rosalind ID: lexf
URL: http://rosalind.info/problems/lexf/

k-mers: nucleotide subsequences
Given two strings s and t of length n, s precedes t in
lexiographical order if s[j] != s[t] and sj < tj in alphabet.

Given: A collection of at most 10 symbols defining an
ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed
from the alphabet, ordered lexicographically (use the
standard order of symbols in the English alphabet).

Sample Dataset:
A C G T
2

Sample Output:
AA
AC
AG
...
TG
TT
'''

path = 'Downloads/rosalind_lexf.txt'
with open(path, 'r') as file:
    data = file.read()
letters = []
for i in data:
    if i.isalpha():
        letters.append(i)
    elif i.isdigit():
        n_length = int(i)
letters.sort(reverse=False)
print(letters)
print(n_length)

temp = []
for letter in letters:
    for other_letter in letters:
        temp.append(letter + other_letter)
print(temp)

i = 2
while i < n_length:
    seqs = temp
    temp = []
    for seq in seqs:
        for letter in letters:
            temp.append(seq+letter)
    if i == n_length-1:
        for seq in temp:
            print(seq)
    for seq in temp:
        if len(seq) <= i:
            temp.remove(seq)
    i += 1