'''
graph is made of nodes (vertices) connected by edges

edge connecting v and w, denoted by v,w or w,v

degree of a node is how many edges connect to it

adjacency list can be used to represent nodes
each row contains two node labels corresponding to a
unique edge

directed graph has directed edges (edge has orientation)
depicted by arrows. tail v and head w represented by
(v,w) but not (w,v)

directed loop is when head and tail are the same (v,v)


For a collection of strings and positive integer k,
overlap graph is O(k). Each string represents a node.
Each string (s) is connected to another string (t)
if in the (s), there is a length k suffix that matches
a length k prefix in (t).

If s != t for any string, demand no directed loops
in overlap graph

Given: A collection of DNA strings in FASTA format
having total length at most 10 kbp.

Return: The adjacency list corresponding to O(3).
You may return edges in any order.
'''

import os
import re
current_dir = os.path.abspath('')
for root, dirs, files in os.walk(current_dir):
    for name in files:
        if name == 'rosalind_grph.txt':
            file_dir = os.path.join(root, name)
with open(file_dir, 'r') as file:
    FASTA_strings = file.read()
matches = re.findall(r'>Rosalind_\d{4}\n[AGCT\n]+',FASTA_strings)
DNA_name_list = []
DNA_string_list = []
DNA_dict = {}
for match in matches:
    match = match.strip('>')
    match = match.split('\n')
    match[1] = match[1] + match[2]
    DNA_name_list.append(match[0])
    DNA_string_list.append(match[1])
    DNA_dict[match[0]] = match[1]
# for i,(k,v) in enumerate(DNA_dict.items()):
#     print(i,k,v)
# DNA_list = zip(DNA_dict.items())
# print(DNA_list)
# for item in DNA_list:
#     print(item[0])
i = 0
counter = 0
while i < len(DNA_string_list):
    for item in DNA_string_list:
        if item[0:3] == DNA_string_list[i][-3:]:
            #print('first',DNA_string_list.index(item),item)
            #print('last',DNA_string_list.index(DNA_string_list[i]),DNA_string_list[i])
            print(DNA_name_list[DNA_string_list.index(DNA_string_list[i])],end=' ')
            print(DNA_name_list[DNA_string_list.index(item)])
            counter+=1
    i+=1

def is_k_overlap(s1, s2, k=3):
    return s1[-k:] == s2[:k]

import itertools
def k_edges(data, k):
    edges = []
    for u,v in itertools.combinations(data, 2):
        u_dna, v_dna = data[u], data[v]

        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u,v))

        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v,u))

    return edges
print('\n\n')
z = k_edges(DNA_dict,3)
for i in z:
    print(i[0],i[1])
print(len(z))
print(counter)