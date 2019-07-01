#!/usr/bin/env python

'''

Title: Independent Alleles
Rosalind ID: LIA
URL: http://rosalind.info/problems/lia/

Two Events A and B are Independent if Pr(A and B) =
Pr(A) x Pr(B).

Given: two (+) integers k (k <= 7) and N (N <= 2^k)
       Begin with Tom who is the 0th generation and is
       Aa Bb. He has two children of generation 1, each
       organism will mate with an AaBb individual and
       have 2 children.

Return: probability that at least N Aa Bb organisms
        will belong to the k-th generation of Tom's
        family tree(don't count the Aa Bb mates at each
        level).Assume that Mendel's second law holds
        for the factors.
'''
import os
from math import factorial
if __name__ == '__main__':
    # if module is imported, this section will not run
    path = os.path.abspath('Downloads/rosalind_lia.txt')
    with open(path,'r') as file:
        nums = file.read().split()
        nums = list(map(int,nums))
        k, N = nums[0], nums[1]
'''
Probability that a child will be Aa
    0% if both parents are AA 
    0% if both parents are aa
    50% if both parents are Aa
    50% if one parent is AA & one parent is Aa
    50% if one parent is aa & one parent is Aa 
Probability that a child will be Bb
    0% if both parents are BB 
    0% if both parents are bb
    50% if both parents are Bb
    50% if one parent is BB & one parent is Bb
    50% if one parent is bb & one parent is Bb 
'''

pr_Aa = 0.5  # one parent is always Aa
pr_Bb = 0.5  # one parent is always Bb
pr_AaBb_Indiv = (pr_Aa*pr_Bb)  # Pr(AaBb) = Pr(Aa) x Pr(Bb)
total_descendants_gen_k = 2**k  # total descendants in generation k

def nCr(n,r):
    return factorial(n)//factorial(r)//factorial(n-r)

total_Less_Min = 0  # all probabilities that less than N will be AaBb
for num in range(0,N):
    total_Less_Min += nCr(total_descendants_gen_k,num)*(0.25**num)*(0.75**(total_descendants_gen_k-num))
    # we know the probability of an AaBb descendant is 0.25
    # therefore the probability of not an AaBb descendant or 0 AaBb descendants is 0.75
print(total_Less_Min)
min_N_gen_k = 1 - total_Less_Min
print(min_N_gen_k)


