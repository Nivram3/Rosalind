#!/usr/bin/env python
'''
Title: Calculating Protein Mass
Rosalind ID: prtm
URL: http://rosalind.info/problems/prtm/
______________________________________________________
APPLICATION SUMMARY:

There are two standard ways of computing the mass of a
residue by summing the masses of its individual atoms.
Its monoisotopic mass is computed by using the
principal (most abundant) isotope of each atom in the
amino acid, whereas its average mass is taken by taking
the average mass of each atom in the molecule (over
all naturally appearing isotopes).

Mass spectrometry is a method used to identify the
chemical makeup of molecules by splitting these
molecules into many small pieces and then analyzing
these snippets. Monoisotopic mass is used more often in
mass spectrometry.

Standard unit of measure in mass spectrometry is
atomic mass units (AMUs) also called daltons.
The mass of a protein is the sum of the monoisotopic
masses of its amino acid residues (residue is molecule
from which a water molecule was removed, all aminos in
a protein are residues) plus the mass of a single
water molecule (whose monoisotopic mass is 18.01056 Da).

We avoid the complication of having to distinguish
between residues and non-residues by only considering
peptides excised from the middle of the protein. Essentially
ignore addition of water. This is a relatively safe
assumption because in practice, peptide analysis is
often performed in tandem mass spectrometry (using
multiple mass spectrometers together)
______________________________________________________
PROBLEM:

A string formed from a weighted alphabet is called a
weighted string, and its weight is equal to the sum of
the weights of its symbols.

The standard weight assigned to each member of the 20-
symbol amino acid alphabet is the monoisotopic mass of
the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P.
'''

import os
path = os.path.abspath('Downloads/rosalind_prtm.txt')
with open(path,'r') as file:
    p_string = file.read()

# also could have made a string and split on white spaces
# then zip it and map each num that is a string to float
# then put all in a dictionary
# Rosalind suggested solution: dict(zip(mmt[::2],map(float,mmt[1::2])))
amino_monoistopic_mass_dict = \
{
    'A':  71.03711,
    'C':  103.00919,
    'D':  115.02694,
    'E':  129.04259,
    'F':  147.06841,
    'G':  57.02146,
    'H':  137.05891,
    'I':  113.08406,
    'K':  128.09496,
    'L':  113.08406,
    'M':  131.04049,
    'N':  114.04293,
    'P':  97.05276,
    'Q':  128.05858,
    'R':  156.10111,
    'S':  87.03203,
    'T':  101.04768,
    'V':  99.06841,
    'W':  186.07931,
    'Y':  163.06333,
}

def protein_mass(protein_string: str):
    mass = 0.0
    for amino in protein_string:
        value = amino_monoistopic_mass_dict.get(amino, "Error")
        if type(value) == float:
            mass += value
    return mass

print(protein_mass(p_string))