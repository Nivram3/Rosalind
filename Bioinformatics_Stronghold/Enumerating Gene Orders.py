'''
Title: Enumerating Gene Orders
Rosalind ID: PERM
URL: http://rosalind.info/problems/perm/

Permutation of length n is ordering of the positive
integers {1,2, ..., n}. For example (5,3,2,1,4) is a
permutation of length 5.

Given: A positive integer.

Return: The total number of permutations of length n,
followed by a list of all such permutations (in any
order).

Eg.

Dataset:
3
Output:
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''

import os
import math
import itertools
path = os.path.abspath('Downloads/rosalind_perm.txt')
with open(path, 'r') as file:
    num = int(file.read())

tot_Perm = math.factorial(num)
print(tot_Perm)
def all_orders(num):
    perm_nums = list(itertools.permutations([x for x in range(1,num+1)]))
    for perm in perm_nums:
        for char in perm:
            print(char, end=' ')
        print()
all_orders(num)
# ////////////////////////////////////////////////////

# does not work for multiple inserts
'''for current_num in range(1, num):
    print('My current num', current_num)
    for index_iterator in range(current_num, num):
        temp_list = [x for x in range(1, num + 1)]
        temp_list.insert(temp_list.index(current_num) + index_iterator, current_num)
        temp_list.remove(current_num)
        for n in range(0, num):
            my_Lists.append(temp_list[0 + n:] + temp_list[:n + 0])
            print(temp_list[0 + n:] + temp_list[:n + 0])
        print('_____')
print(len(my_Lists))'''
# /////////////////////////////////////////////////////

# Stack Overflow Recursion Solution
def permutations(_string):
    permutations = []
    def step(done, remain):
        if remain == '':
            permutations.append(done)
        else:
            for i, char in enumerate(remain):
                rest = remain[:i] + remain[i + 1:]
                step(done + char, rest)
    step("", _string)
    return permutations
