'''
3 red marbles
2 blue marbles
2 reds in a row = (3/5)(2/4) = 3/10
2 blues in a row = (2/5)(1/4) = 1/10
1 red 1 blue = (3/5)(2/4) = 3/10
1 blue 1 red = (2/5)(3/4) = 3/10

Probability that 2nd marble is blue is 4/10

Given 3 positive integers k,m,n representing a pop
with k + m + n organisms,
k indivs are homozygous dominant
m indivs are heterozygous
n indivs are homozygous recessive

Return the probability that two randomly selected
mating organisms will produce an individual possessing
a dominant allele (and thus displaying the dominant
phenotype). Assume that any two organisms can mate.
'''
import os
path = os.path.abspath("Downloads/rosalind_iprb.txt")
with open(path,'r') as file:
    kmn = file.read()
AA_indivs, Aa_indivs, aa_indivs = map(int,kmn.split())

total_indivs = AA_indivs + Aa_indivs + aa_indivs

AA_AA = (AA_indivs/total_indivs)*(AA_indivs-1)/(total_indivs-1)
AA_Aa = (AA_indivs/total_indivs)*(Aa_indivs)/(total_indivs-1)
AA_aa = (AA_indivs/total_indivs)*(aa_indivs)/(total_indivs-1)

Aa_Aa = (Aa_indivs/total_indivs)*(Aa_indivs-1)/(total_indivs-1)
Aa_AA = (Aa_indivs/total_indivs)*(AA_indivs)/(total_indivs-1)
Aa_aa = (Aa_indivs/total_indivs)*(aa_indivs)/(total_indivs-1)

aa_aa = (aa_indivs/total_indivs)*((aa_indivs-1)/(total_indivs-1))
aa_Aa = (aa_indivs/total_indivs)*((Aa_indivs)/(total_indivs-1))
aa_AA = (aa_indivs/total_indivs)*((AA_indivs)/(total_indivs-1))

min_1_dominant_allele_in_organism = AA_AA + AA_Aa + AA_aa + Aa_Aa*0.75 + Aa_AA + Aa_aa*0.5 + aa_Aa*0.5 + aa_AA
print(min_1_dominant_allele_in_organism)

'''
USE DOM and REC Alleles
k,m,n=16,21,18
tot=(k+m+n)*2
dom=k*2+m
rec=n*2+m
print(1-(rec/tot)*((rec-1)/(tot-1)))

Calculate Recessive Trait then subtract from 1
prob of recessive allele = 1/2*(m/(k+m+n)) + n/(k+m+n)
50% from hetero and 100% from recessive 
then multiply this value by probability of another recessive
allele 

Return a random element from a sequence
and return a unique list of (pop,k) k elements long 
import random
k, m, n = map(int, input().split())
population = k * ["AA"] + m * ["Aa"] + n * ["aa"]
count = 0
for i in range(10000):
  count += 'A' in [random.choice(x) for x in random.sample(population, 2)]
print(count / 10000)

random.sample used for random sampling without replacement
same output if random.choice not included
'''