'''
__Author__ = 'Marvin Yan'

Sequence is ordered collection of objects which may
repeat
Sequences can be finite or infinite

Recurrence Relation
- define terms of a sequence with respect to previous
term values
The Fibonacci sequence
- A sequence of numbers defined by the recurrence
relation , where we set the starting values .
////////////////////////////////////////////////////

Any given month will contain the rabbits that were
alive the previous month, plus any new offspring.

The number of offspring in any month is equal to the
number of rabbits that were alive two months prior.

When finding the -th term of a sequence defined by a
recurrence relation, we can simply use the recurrence
relation to generate terms for progressively larger
values of. This problem introduces us to the
computational technique of dynamic programming, which
successively builds up solutions by using the answers
to smaller cases.

Given: Positive integers n <= 40 and k <= 5.

Return: The total number of rabbit pairs that will be
present after n months, if we begin with 1 pair and
in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs.
'''
import os

abs_path = os.path.abspath('Downloads/rosalind_fib.txt')
with open(abs_path, 'r') as file:
    data = file.read()
    data = data.split()
num_of_months = int(data[0])
offspring_pairs = int(data[1])
# while True:
#     try:
#         num_of_months = int(input('Number of months for rabbits to reproduce:\n'))
#         offspring_pairs = int(input('Number of offspring pairs from a pair of mature rabbits:\n'))
#         if num_of_months > 0 and offspring_pairs > 0:
#             break
#         else:
#             print('One or more of your inputs was less than or equal to 0')
#             continue
#     except ValueError:
#         print('One of your inputs was not an integer')
#         continue

rabbit_pop = [1,1]
i = 2
while i < num_of_months:
    new_pop = rabbit_pop[i-2]*offspring_pairs + rabbit_pop[i-1]
    rabbit_pop.append(new_pop)
    i+=1
print(rabbit_pop)
print(rabbit_pop[-1])
