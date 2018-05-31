#!/usr/bin/env python
#######Compute using python data structures########
import sys
#####Timing the code######
from datetime import datetime
startTime=datetime.now()
#########################
def freqArray(text,k):
    freq_array={}
    for i in xrange(len(text)-k+1):#Collecting kmer pattern
        pattern=text[i:i+k]
        if freq_array.get(pattern,0)==0:#If no such kmer existed!
            freq_array[pattern]=1
        else:
            freq_array[pattern]+=1#increment kmer count by 1
    return freq_array

def clumpFind(genome,k,l,t):
        clump=[] 
        freq_array=freqArray(genome[0:l],k)#freq_array from window 1
        for pattern,freq in freq_array.items():
            if freq>=t:
                clump.append(pattern)
        ####Update freq_array for Window 2 onwards...
        for i in xrange(1,len(genome)-l+1):#Window 2 onwards....
            first_pattern=genome[i-1:i-1+k]
            last_pattern=genome[i+l-k:i+l]
            freq_array[first_pattern]-=1
            if freq_array.get(last_pattern,0)==0:#the last pattern in new window never existed in previous pattern:
                freq_array[last_pattern]=1#then add that new last pattern
            else:
                freq_array[last_pattern]+=1
            if freq_array[last_pattern]>=t:
                clump.append(last_pattern)
        return list(set(clump))
##Test Data######
#genome='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k=9
l=500
t=3
genome=''
fh=open(sys.argv[1])
for line in fh:
   line=line.rstrip().rstrip('')
   genome=genome+line
#k=int(raw_input("Enter k:"))
#l=int(raw_input("Enter l:"))
#t=int(raw_input("Enter t:"))
clumps=clumpFind(genome,k,l,t)
c=0
for clump in clumps:
    c=c+1
    print clump,
print c 
#print datetime.now()-startTime
