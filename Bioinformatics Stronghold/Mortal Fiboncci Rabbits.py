'''
Fibonacci sequence, which has the recurrence relation,
Fn = F(n-1) + F(n-2) assuming that F1 = 1 and F2 = 1
Assumed that each pair of rabbits reaches maturity in
one month and produces a single pair of offspring that
was 1 male and 1 female

Modify for rabbits dying out in a fixed num of months.


Given: Positive integers n <= 100 and m <= 20.

Return: The total number of pairs of rabbits that will
remain after the n-th month if all rabbits live for
m months.
'''

# n = 6 and m = 3 should give 4 pairs left

import os
file_name = 'rosalind_fibd.txt'
for root, dirs, files in os.walk(r'C:\Users\marvi\PycharmProjects'):
    for name in files:
        if name == file_name:
            file_loc = os.path.join(root, name)
with open(file_loc,'r') as f:
    nm = f.read().split()
    n,m = int(nm[0]),int(nm[1])
print(n,m)

rabbit_pair_adult = [0,1]
rabbit_pair_baby = [1,0]
rabbit_pair_total = [1,1]
i = 2

while i < n:
    if len(rabbit_pair_adult) < m:
        new_adult_pop = rabbit_pair_baby[i-1] + rabbit_pair_adult[i-1]
        new_baby_pop = rabbit_pair_adult[i-1]
        rabbit_pair_baby.append(new_baby_pop)
        rabbit_pair_adult.append(new_adult_pop)
        rabbit_pair_total.append(new_baby_pop+new_adult_pop)
        i+=1
    else:
        new_adult_pop = rabbit_pair_baby[i-1] + rabbit_pair_adult[i-1] - rabbit_pair_baby[i-m]
        new_baby_pop = rabbit_pair_adult[i-1]
        rabbit_pair_baby.append(new_baby_pop)
        rabbit_pair_adult.append(new_adult_pop)
        rabbit_pair_total.append(new_baby_pop+new_adult_pop)
        i += 1
print('adult pairs\t ',rabbit_pair_adult)
print('baby pairs\t ',rabbit_pair_baby)
print('total rabbits',rabbit_pair_total)
print(rabbit_pair_total[-1])