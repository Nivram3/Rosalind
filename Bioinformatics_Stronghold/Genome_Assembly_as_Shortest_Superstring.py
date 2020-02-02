'''
Title: Genome Assembly as Shortest Superstring
Rosalind ID: long
URL: http://rosalind.info/problems/long/

Background on Genome Sequencing:
- Humans share approximately 99.9% of the same nucleotides
on the genome.
- Genome sequencing is the process of determining an
organism's complete genome.
- Current chemical methods identify small sequences
called reads (substring of genome for fragment assembly)
- By obtaining multiple reads, we can reconstruct the
genome (process of fragment assembly)

Problem:
- For a collection of strings, a larger string containing
all the smaller strings is called a superstring
- Principle of parsimony assumes shortest superstring
is the candidate chromosome

Given: <= 50 DNA strings of equal length from the same
strand of a linear chromosome in FASTA format

Return: the shortest superstring containing all given strings
'''
from Bio import SeqIO
file = 'Downloads/rosalind_long.txt'
records = list(SeqIO.parse(file, 'fasta'))
my_seqs_3 = [r.seq for r in records]

'''
Approach 3 (Failed attempts below)

Given:
- a list of strings 

Return: 
- shortest superstring (contains all strings within list)

Method:

1.
- for each string, find other strings that match its front and end
- record index of that string as a dictionary key and the front matches and end matches in 2 lists as a value
- for the front matches of that string, find the one that has the longest match
- for the end matches of that string, find the one that has the longest match

2.
- once the dictionary is complete, if the index of the longest front match of String S is String R, 
and if the index of longest end match of String R is String S, and append the two together 
- if not, resolve later (there should be 2 which are front and end string
- assemble order of seqs and append them all together accounting for regions of overlap

* if there is a case where shortest superstring requires a duplicate of a string, will not work
* if there are substrings, will not work
'''
def seq_longest_front_end_match(seqs):
    all_matches = dict()

    for seq in seqs:
        # find matches at beginning for end of another seq
        end_matches = []
        for other_seq in seqs[:seqs.index(seq)] + seqs[seqs.index(seq)+1:]:
            j = 1
            while j <= len(seq):
                if seq[:j] == other_seq[len(other_seq)-j:]:
                    end_matches.append((len(seq[:j]),seqs.index(other_seq)))
                j += 1
        end_matches = sorted(end_matches, key=lambda x: x[0], reverse=True)
        # print('end',seqs.index(seq),end_matches)
        if len(end_matches) < 2:
            try:
                all_matches[seqs.index(seq)] = [end_matches]
            except:
                continue
        else:
            all_matches[seqs.index(seq)] = [[end_matches[0],end_matches[1]]]

        # find matches at end for beginning of another sequence
        front_matches = []
        for other_seq in seqs[:seqs.index(seq)] + seqs[seqs.index(seq)+1:]:
            k = 1
            while k <= len(seq):
                # if seq[k:] == other_seq[:len(other_seq) + 1 - k]:
                #     front_matches.append((len(seq[k:]),seqs.index(other_seq)))
                if other_seq[:k] == seq[len(seq)-k:]:
                    front_matches.append((len(seq[:k]),seqs.index(other_seq)))
                k += 1
        front_matches = sorted(front_matches, key=lambda x: x[0], reverse=True)
        # print('front',seqs.index(seq),front_matches)

        if len(front_matches) < 2:
            try:
                all_matches[seqs.index(seq)].append(front_matches)
            except:
                if len(front_matches) == 0:
                    continue
                elif seqs.index(seq) not in all_matches.keys():
                    all_matches[seqs.index(seq)] = [front_matches]
        else:
            all_matches[seqs.index(seq)].append([front_matches[0], front_matches[1]])
    # for k,v in all_matches.items():
    #     print(k,v)

    return all_matches

def seq_assembly(seqs):

    all_matches = seq_longest_front_end_match(seqs)
    # print('longest matches complete',all_matches)
    assembly_order = [0]
    keys = list(all_matches.keys())
    keys.remove(0)

    initial_front = all_matches.get(0)  # values
    parent_front_match = initial_front[0][0][1]  # index
    initial_end = all_matches.get(0)
    parent_end_match = initial_end[1][0][1]  # index

    while len(keys) != 0:
        front_matching_values = all_matches.get(parent_front_match)
        front_matchs_first_end_key = front_matching_values[1][0][1]

        if all_matches.get(front_matchs_first_end_key) == initial_front:
            assembly_order.insert(0, parent_front_match)
            keys.remove(parent_front_match)
            initial_front = all_matches.get(parent_front_match)
            parent_front_match = front_matching_values[0][0][1]

        end_matching_values = all_matches.get(parent_end_match)
        end_matchs_first_front_key = end_matching_values[0][0][1]
        if all_matches.get(end_matchs_first_front_key) == initial_end:
            assembly_order.append(parent_end_match)
            keys.remove(parent_end_match)
            initial_end = all_matches.get(parent_end_match)
            parent_end_match = end_matching_values[1][0][1]

    # print(assembly_order)
    final_string = ''
    for index in assembly_order:
        values = all_matches.get(index)
        length_of_match = values[1][0][0]
        length_of_seq = len(seqs[index])
        if index != assembly_order[-1]:
            final_string += seqs[index][:length_of_seq-length_of_match]
        else:
            final_string += seqs[index]
        # print(seqs[index][:length_of_seq-length_of_match])
    return final_string

if __name__ == '__main__':
    seqs_test = ['TGGAAAAAACATTTGAC',
                          'CATTTGACGGAC',
                             'TTGACGGACTCC',
                                      'TCCGGATCGATC',
                                         'GGATCGATCTAACTG',
                                                   'AACTGGCAGCGCTGA',
                                                       'GGCAGCGCTGAATATTTGATGG',
                                                               'TGAATATTTGATGGAGACCCC']
    #            'TGGAAAAAACATTTGACGGACTCCGGATCGATCTAACTGGCAGCGCTGAATATTTGATGGAGACCCC
    print(seq_assembly(seqs_test))
    print(seq_assembly(my_seqs_3))


#///////////////////////////////////////////////////////////////////////////////////////////////////////
# PREVIOUS FAILED ATTEMPTS

'''
Approach 1

# def find_matches_between_strings(seqs):
#     all_matches = []
#
#     for seq in seqs:
#         j = 0
#         for other_seq in seqs[seqs.index(seq) + 1:]:
#             matches = ['','']
#             index = 0
#             length = 2
#             j += 1
#             while index <= len(seq) - 1 and (index + length) <= len(seq):
#                 # if sorted(matches, key=len)[-2] == sorted(matches, key=len)[-1][:-1] and len(sorted(matches, key=len)[-1]) > 10:
#                 #     break
#                 if seq[index:index + length] in other_seq:
#                     if seq[index:index + length] not in matches:
#                         matches.append(seq[index:index + length])
#                     length += 1
#                 else:
#                     index += 1
#                     length = 2
#             print(j,matches)
#             # print(seq,other_seq,max(matches, key=len))
#             for match in matches:
#                 if len(match) == len(max(matches, key=len)):
#                     # print(seq, other_seq, match)
#                     all_matches.append(match)
#     all_matches = [x for x in list(set(all_matches)) if len(x) >= len(max(all_matches, key=len))/2]
#     return all_matches
#
# # callback
# def find_shortest_superstring(func,seqs):
#     # print(sum(len(i) for i in func(seqs)) / len(func(seqs)))
#     while len(seqs) > 1:
#         longest_matches = find_matches_between_strings(seqs)
#         # for i in func(seqs):
#         #     if len(i) >= sum(len(i) for i in func(seqs))/len(func(seqs)):
#         #         longest_matches.append(i)
#         for substring in longest_matches:
#             if len([s for s in longest_matches if substring in s]) > 1:
#                 longest_matches.remove(substring)
#         for substring in seqs:
#             if len([s for s in seqs if substring in s]) > 1:
#                 seqs.remove(substring)
#         print('seqs',seqs)
#         print('longest_matches', longest_matches)
#         front_matches = []
#         end_matches = []
#         for match in longest_matches:
#             for seq in seqs:
#                 if match == seq[-len(match):]:
#                     end_matches.append([match,seq])
#                 if match == seq[:len(match)]:
#                     front_matches.append([match,seq])
#         print('front',front_matches)
#         print('end',end_matches)
#         seqs.clear()
#         for front_match in front_matches:
#             for end_match in end_matches:
#                 if front_match[0] == end_match[0]:
#                     print(front_match,end_match)
#                     print(end_match[1][:len(end_match[1])-len(end_match[0])] + front_match[1])
#                     seqs.append(end_match[1][:len(end_match[1])-len(end_match[0])] + front_match[1])
#         print('NEXT seqs',seqs)
#     return 'RESULT', seqs[0]
'''

'''
Approach 2

Find longest matches that belong to ends and beginnings for seqs
Once found, combine the two seqs together, new set of data available and repeat until only one seq left

my_seqs_3 = [r.seq for r in records]

def genome_assembly(seqs):
    my_seqs = seqs
    seqs_length = len(my_seqs)
    while seqs_length > 1:
        my_seqs = seq_longest_front_end_match(my_seqs)
        seqs_length = len(my_seqs)
    return my_seqs

def seq_longest_front_end_match(seqs):
    all_matches_front_of_seq = []
    # all_matches_front_of_other_seq = []
    for seq in seqs:
        matches = []
        for other_seq in seqs[:seqs.index(seq)] + seqs[seqs.index(seq)+1:]:
            j = 1
            while j <= len(seq):
                if seq[:j] == other_seq[len(other_seq)-j:]:
                    matches.append((seq[:j],seqs.index(seq),seqs.index(other_seq)))
                j += 1
        # print('matches',matches)
        try:
            all_matches_front_of_seq.append(max(matches, key=lambda item: len(item[0])))
        except ValueError:
            continue
    # for seq in seqs:
    #     matches = []
    #     for other_seq in seqs[seqs.index(seq) + 1:]:
    #         j = 1
    #         while j <= len(seq):
    #             if other_seq[:j] == seq[len(seq)-j:]:
    #                 matches.append((other_seq[:j],seqs.index(other_seq),seqs.index(seq)))
    #             j += 1
    #     try:
    #         # all_matches_front_of_other_seq.append(max(matches[0], key=len))
    #         all_matches_front_of_other_seq.append(max(matches, key=lambda item: len(item[0])))
    #     except ValueError:
    #         continue

    print('seq',len(all_matches_front_of_seq))
    for match in all_matches_front_of_seq:
        print(len(match[0]), match)
    # print('other seq',len(all_matches_front_of_other_seq))
    # for match in all_matches_front_of_other_seq:
    #     print(len(match[0]), match)

    new_seqs = []
    for match in list(set(all_matches_front_of_seq)):
        if len(match[0]) >= (sum(len(x) for x in seqs)/len(seqs))/9:
            new_seqs.append(seqs[match[2]][:len(seqs[match[2]]) - len(match[0])] + seqs[match[1]])
    print(new_seqs)
    print('TOTAL NEW SEQS', len(new_seqs))
    print('\n\n\n')
    return new_seqs
# print(genome_assembly(my_seqs_1))
# a = seq_longest_front_end_match(my_seqs_1)
# b = (seq_longest_front_end_match(a))
# print(seq_longest_front_end_match(b))
print(genome_assembly(my_seqs_3))
'''