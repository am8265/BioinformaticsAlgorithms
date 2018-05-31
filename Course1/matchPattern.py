#!/usr/bin/env python
#######Match a Pattern in a Genome##############
import sys
import re
def patternMatch(genome,pattern):
    pos=0
    positions=[]
    while True:
        pos=genome.find(pattern,pos)
        if pos==-1:
            break;
        positions.append(pos)
        pos=pos+1
    if len(positions)==0:
        return "Pattern Doesn't exist in the Genome!"
    else:
        return positions
genome=''
#pattern=raw_input("Enter a pattern:")
pattern='ATGATCAAG'
fh=open(sys.argv[1],'r')
for line in fh:
    line=line.rstrip().strip('')
    line=line.upper()
    genome=genome+line
fh.close()
for pos in patternMatch(genome,pattern):
    print '%d '%(pos),

