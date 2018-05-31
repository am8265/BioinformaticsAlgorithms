#!/usr/bin/env python
#############Aproximate pattern matching using the hamming distance function#######
import sys
import re
from datetime import datetime
from hamming import hamming_distance
def aprxPattern(text,pattern,d=0):
    '''text-Nucleotide sequence\
    pattern-pattern to be matched 
    d-default value 0 other wise user entered hamming distance value\
    The function returns locations of the aproximate matches of the pattern in the text provided '''
    l=len(text)
    k=len(pattern)
    pos=[]
    for i in xrange(l-k+1):
        kmer=text[i:i+k]
        if hamming_distance(pattern,kmer)<=d:
          pos.append(i)
        else:
            pass
    return len(pos)
######Test Data##########
#startTime=datetime.now()
#pattern='CCC'
#genome='GAATCCGCCAAGTACCAAGATGTAAGTGAGGAGCGCTTAGGTCTGTACTGCGCATAAGCCTTAACGCGAAGTATGGATATGCTCCCCGGATACAGGTTTGGGATTTGGCGGTTACCTAAGCTAACGGTGAGACCGATATGACGAGGTTCCTATCTTAATCATATTCACATACTGAACGAGGCGCCCAGTTTCTTCTCACCAATATGTCAGGAAGCTACAGTGCAGCATTATCCACACCATTCCACTTATCCTTGAACGGAAGTCTTATGCGAAGATTATTCTGAGAAGCCCTTGTGCCCTGCATCACGATTTGCAGACTGACAGGGAATCTTAAGGCCACTCAAA'
#d=2
#genome='CATGCCATTCGCATTGTCCCAGTGA'
#fh=open(sys.argv[1])
#for line in fh:
#    line=line.rstrip().rstrip('')
#    genome+=line
#fh.close()
#pattern=raw_input("Enter pattern to be searched")
#d=int(raw_input("Enter number of mismatches allowed"))
#for pos in aprxPattern(genome,pattern,d):
#    print pos,
#print len(aprxPattern(genome,pattern,2))
#print datetime.now()-startTime

    
