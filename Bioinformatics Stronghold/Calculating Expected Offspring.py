'''
For variable x in range from 1 - n,
the expected value of x is its average over many trials

Example, x is number on a six-sided die, the avg
should be 3.5 even though you can't get 3.5.
formula is: sigma from k = 1 to 6, k*(probability of k)
so.. 1(1/6) + 2(1/6) + 3(1/6) etc
"uniform random variable, equal probabilities"

Simplified formula if X is a uniform random variable
with min of a and max of b, Expected(x) = a + b /2
eg. die, 1+6/2 = 3.5

Given:

Six nonnegative integers, each of which does not
exceed 20,000. The integers correspond to the number
of couples in a population possessing each genotype
pairing for a given factor. In order, the six given
integers represent the number of couples having the
following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return:
The expected number of offspring displaying the
dominant phenotype in the next generation, under the
assumption that every couple has exactly two offspring.

Eg. 1 0 0 1 0 1 gives 3.5
1*2 + 3/4*2 + 0*2 = 2 + 1.5 = 3.5
'''
import os
path = os.path.abspath('Downloads/rosalind_iev.txt')
with open(path,'r') as file:
    couple_frequencies = file.read().split()

for index, couple in enumerate(couple_frequencies):
    if couple.isdigit():
        couple_frequencies[index] = int(couple)
    #    parentCounts = [int(x) for x in file.read().split()]
    # better solution
print(couple_frequencies)

frequency_dict = {}
couple_pairings = ['AAAA','AAAa','AAaa','AaAa','Aaaa','aaaa']
for couple in couple_pairings:
    temp_frequency_dom = []
    temp_frequency_dom.append(couple[0]+couple[2])
    temp_frequency_dom.append(couple[0] + couple[3])
    temp_frequency_dom.append(couple[1] + couple[2])
    temp_frequency_dom.append(couple[1] + couple[3])
    i = 0
    for offspring in temp_frequency_dom:
        if 'A' in offspring:
            i += 0.25
    frequency_dict[couple] = i
print(frequency_dict)

i = 0
final_prob = 0
while i < len(couple_frequencies):
    final_prob += couple_frequencies[i]*frequency_dict.get(couple_pairings[i])*2
    i+=1
print(final_prob)
