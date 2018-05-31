#!/usr/bin/env python
######Computing GC Skew of DNA  sequence#############
##########Also Computing minimum skew#################
import sys
def skew(seq):
    i=0
    skew=0
    allSkew=[0]
    for nuc in seq:
        i=i+1
        if nuc=='G':
            skew+=1
        elif nuc=='C':
            skew-=1
        allSkew.append(skew)
    return allSkew
#genome=''
#fh=open(sys.argv[1])
#for line in fh:
#    line=line.rstrip().strip('')
#    genome=genome+line
skew=skew('GCATACACTTCCCAGTAGGTACTG')
minimum=min(skew)
pos=-1
for vals in skew:
    pos+=1
    if vals==minimum:#print the position in the genome where skew value is MINIMUM!
        print pos,

print skew
