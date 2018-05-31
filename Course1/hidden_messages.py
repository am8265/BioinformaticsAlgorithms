#!/usr/bin/env python
import math
def neighbors(pattern,d):
    '''Function takes in a k-mer pattern and hamming distance upto d and returns count of all such possible neighbors and neighbors themselves'''
    k=len(pattern)
    neighbors_ct=0
    for i in xrange(d):
        neighbors_ct+=(3**(i+1))*math.factorial(k)/((math.factorial(k-i-1))*math.factorial((i+1)))
    return (neighbors_ct+1)
print neighbors('ACCACACACAATG',13)
