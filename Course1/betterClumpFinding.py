#!/usr/bin/env python
import sys
from datetime import datetime
from freq_array import computing_freq
#from number_to_pattern import number_pattern#This could be limiting!think about changing the algorithm
from patt_to_number import pattern_to_number
startTime=datetime.now()
def BetterClumpFinding(Genome,k,t,l):
    freq_pattern=[]
    for i in xrange(1,(4**k)+1):
        clump=[0]*i
    text=genome[0:l]#use window 1 as a Reference!
    freqArray=computing_freq(text,k)#We compute frequency array only ONCE i.e for the WINDOW 1
    for i in xrange(4**k):
        if freqArray[i]>=t:
            clump[i]=1
    for i in xrange(1,len(genome)-l+1):#Starting from window 2 onwards:
        firstPattern=genome[i-1:i-1+k]
        index=pattern_to_number(firstPattern)
        freqArray[index]=freqArray[index]-1#We didn't CALL Computing_freq again!
        lastPattern=genome[i+l-k:i+l]
        index=pattern_to_number(lastPattern)
        freqArray[index]=freqArray[index]+1
        if freqArray[index]>=t:#compare the last index only as previous ones been accounted before
            clump[index]=1
    for i in xrange(4**k):
        if clump[i]==1:
            #pattern=number_pattern(i,k)
            freq_pattern.append(i)#lets return the index for now
            
    return freq_pattern
#####test Data#########
#genome='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'


genome=''
fh=open(sys.argv[1])
for line in fh:
   line=line.rstrip().rstrip('')
   genome=genome+line
k=int(raw_input("Enter k:"))
l=int(raw_input("Enter l:"))
t=int(raw_input("Enter t:"))
print BetterClumpFinding(genome,k,t,l)
print datetime.now()-startTime
