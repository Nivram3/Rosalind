'''
Title: Longest Increasing Subsequence
Rosalind ID: lgis
URL: http://rosalind.info/problems/lgis/

Problem:
Subsequence of a permutation is a collection of elements
in the permutation in the order they appear.
Eg. (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

An increasing subseqnence is if the elements increase.
Eg. Given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9),
an increasing subsequence is (2, 6, 7, 9).

Given: A positive integer n ≤ 10000 followed by a
permutation π of length n.

Return: A longest increasing subsequence of π,
followed by a longest decreasing subsequence of π.

/////////////////////////////////////////////////////
SOLUTIONS ARE THE BOTTOM 3 FUNCTIONS
- longest_increasing_subsequence, calc_LIS, calc_LDS
- calc_LIS and calc_LDS not efficient code
/////////////////////////////////////////////////////
'''

# BRUTE FORCE METHOD TAKES TOO LONG, BELOW METHOD ALSO DOES NOT WORK
# overall_max_len_sub = []
# for num in sequence:
#     longest_temp = [num]
#     i = 0
#     while i < int(length) - sequence.index(num):
#         initial_index = sequence.index(num)
#         if int(sequence[initial_index + i]) > int(longest_temp[-1]):
#             # print(sequence[initial_index + i])
#             longest_temp.append(sequence[initial_index + i])
#         i += 1
#     if len(longest_temp) > len(overall_max_len_sub):
#         overall_max_len_sub = longest_temp
#         print(overall_max_len_sub)

# SOLVE USING DYNAMIC PROGRAMMING
# (store results of subproblems, do not recompute)


# https://www.dailycodingproblem.com/blog/longest-increasing-subsequence/
# provides length of LIS
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)
print(longest_increasing_subsequence([5,3,4,7]))



# FULL SOLUTION
# https://stackoverflow.com/questions/49985779/find-increasing-and-decreasing-subsequence-in-an-array-python
# not optimal (stores every value, memory issues)
with open('Downloads/rosalind_lgis.txt','r') as file:
    data = file.read()
    print(data)

length, sequence = data.split('\n')[0], data.split('\n')[1].split()
sequence = [int(i) for i in sequence]

# def findLIS(array):
#     LIS = []
#     for i in array[::-1]:
#         for j in LIS[:]:
#             if i <= j[0]:
#                 LIS.append([i] + j)
#         LIS.append([i])
#     longest_array = []
#     for l in LIS:
#         if len(l) > len(longest_array):
#             longest_array = l
#     return longest_array
#
# def findLDS(array):
#     LDS = []
#     for i in array[::-1]:
#         for j in LDS[:]:
#             if i >= j[0]:
#                 LDS.append([i] + j)
#         LDS.append([i])
#     longest_array = []
#     for l in LDS:
#         if len(l) > len(longest_array):
#             longest_array = l
#     return longest_array

# OPTIMAL SOLUTION
# https://rosettacode.org/wiki/Longest_increasing_subsequence#Python
def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if (X[M[mid]] < X[i]):
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if (newL > L):
            L = newL
    # print('L',L)
    S = []
    k = M[L]
    # print('k',k)
    for i in range(L - 1, -1, -1):
        # print('k',k)
        # print(X[k])
        S.append(X[k])
        k = P[k]
    S.reverse()
    for i in S:
        print(i,end=' ')
    print('length:', len(S))
    return '' #S[::-1]

# https://www.youtube.com/watch?v=4fQJGoeW5VE Solution
def calc_LIS(array):
    L = [[array[0]]]+[[]]*(len(array)-1)
    for i in range(1, len(array)):
        for j in range(0, i):
            # find longest array L where array[j] < array[i]
            # find longest L[j] whose tail array[j] < array[i]
            if array[j] < array[i]:
                if len(L[i]) < len(L[j]):
                    L[i] = L[j]
        L[i] = L[i] + [array[i]]
    max_LIS = []
    for LIS in L:
        if len(LIS) > len(max_LIS):
            max_LIS = LIS
    for num in max_LIS:
        print(num, end= ' ')
    print('length:', len(max_LIS))
    return ''
def calc_LDS(array):
    L = [[array[0]]]+[[]]*(len(array)-1)
    for i in range(1, len(array)):
        for j in range(0, i):
            # find longest array L where array[j] < array[i]
            # find longest L[j] whose tail array[j] < array[i]
            if array[j] > array[i]:
                if len(L[i]) < len(L[j]):
                    L[i] = L[j]
        L[i] = L[i] + [array[i]]
    max_LDS = []
    for LDS in L:
        if len(LDS) > len(max_LDS):
            max_LDS = LDS
    for num in max_LDS:
        print(num, end= ' ')
    return ''
# print(calc_LIS(sequence))
# print(calc_LDS(sequence))

if __name__ == '__main__':
    'TESTS'
    print(longest_increasing_subsequence(sequence))
    print(calc_LIS(sequence))
    print(calc_LDS(sequence))
    # print(list(reversed(longest_increasing_subsequence(sequence))))
    print([[]]*5)
    # print(longest_increasing_subsequence([5,2,3,7,4,6]))


    import random
    seq4 = [random.randint(0,10000) for i in range(0,10000)]
    print(seq4) # will be unique numbers
    print(calc_LIS(seq4))
    print(longest_increasing_subsequence(seq4))