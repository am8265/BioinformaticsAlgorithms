#!/usr/bin/env python
#########Pattern count############
import sys

def PatternCount(text,pattern):
    '''Text is string of ATGCCACA.....' where we want to locate a Pattern of length kmer'''
    count=0
    k=len(pattern)
    n=len(text)-k+1
    for i in xrange(0,n):
        #print i
        if text[i:i+k]==pattern:
            count=count+1
        
    return count
#pattern=raw_input("Enter a pattern:")
#text=''
#3fh=open(sys.argv[1],'r')
#for line in fh:
#    line=line.rstrip('\n').strip('')
#    text=text+line
#text=text.upper()#convert all into upper case letters
#pattern=pattern.upper()
#print pattern
#print text
#print PatternCount(text,pattern)
