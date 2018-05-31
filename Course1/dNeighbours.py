#!/usr/bin env python
##########This Program computes the Neighborhood of a kmer pattern#########
from hamming import hamming_distance 
def suffix(pattern):
    return pattern[1:]
def first_symbol(pattern):
    return pattern[0]

#####Recursive Function###########
######Function calling itself#############
def neighbors(pattern,d):
    if d==0:
        return pattern
    elif len(pattern)==1:
        return ['A','C','G','T']
    neighborhood=[]#should contain all d neighborhood k mer patterns 
    suffixNeighbors=neighbors(suffix(pattern),d)
    for pat in suffixNeighbors:
        if hamming_distance(suffix(pattern),pat)<d:
            for nuc in ['A','C','G','T']:
                neighborhood.append(nuc+pat)
        else:
            neighborhood.append(first_symbol(pattern)+pat)
    return neighborhood

#pattern='GGCCCAGAG'
#d=3
#print neighbors(pattern,d)
