#!/usr/bin/env python
import sys
import re
def hamming_distance(seq1,seq2):
    mismatch_pos=[]
    for i in xrange(len(seq1)):
        if seq1[i]!=seq2[i]:#Checking for mismatch
            mismatch_pos.append(i)
    return len(mismatch_pos)
#####Test Cases###########
#print hamming_distance('CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT','CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG')
#print hamming_distance('CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT','CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG')
