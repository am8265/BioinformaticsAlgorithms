#!/usr/bin/env python
from numpy.random import choice
def randomSequence(l):
    '''l-length of nucleotide sequence must be an integer or float
    the function would return a random sequence of same length'''
    prob_dist=[0.25,0.25,0.25,0.25]#uniform probability distribution for 'A','T','G's and 'C's 
    patterns=['A','T','G','C'] 
    random_sequence=''
    for i in xrange(l):
        random_sequence+=choice(patterns,1,p=prob_dist)[0]
    return random_sequence

print randomSequence(10)
