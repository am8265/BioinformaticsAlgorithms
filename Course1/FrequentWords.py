#!/usr/bin/env python
#####Frequent Words Problem#########
import re
import sys
from PatternCount import PatternCount# A module that has a function that computes count of pattern in a given Text
def FrequentWords(text,k):
    count=[]#a list to store the pattern count for each kmers
    freq_patterns=[]#stores Most frequent kmer patterns
    for i in xrange(len(text)-k+1):
        pattern=text[i:i+k]
        count.append(PatternCount(text,pattern))
    maxCount=sorted(count)[-1]#maximum VALUE of occurence of a kmer pattern in Text
    for i in xrange(len(text)-k+1):
        if count[i]==maxCount:
            freq_patterns.append(text[i:i+k])#There would be many duplicates
        freq_patterns=list(set(freq_patterns))#removing all duplicates by using set function and converting it back to list
    return freq_patterns
#text=''
k=int(raw_input("Enter k for kmer:"))
#fh=open(sys.argv[1],'r')
#for line in fh:
#    line=line.rstrip().strip('')
#    text=text+line
print FrequentWords('TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT',k)


