#!/usr/bin/env python
from dNeighbours import neighbors
from aprxPatternMatch import aprxPattern
from datetime import datetime
from reverseComplement import revComplement
import sys
def freqWordsMismatch(text,k,d):
    close=[]
    for i in xrange(len(text)-k+1):
        neighborhood=neighbors(text[i:i+k],d)
        close.extend(neighborhood)
    close=list(set(close))#removing any duplicates!
    pat_ct=dict()
    for pat in close:
        pat_ct[pat]=aprxPattern(text,pat,d)+aprxPattern(text,revComplement(pat),d)
    sort_pat=sorted(pat_ct.items(), key=lambda x:x[1])
    for key,val in sort_pat[-1::-1]:
        if val==sort_pat[-1][1]:
            print key,
genome=''
fh=open(sys.argv[1])
k=7
d=3
for line in fh:
    line=line.rstrip('\n').strip('')
    genome=genome+line
fh.close()
freqWordsMismatch(genome,k,d)

#freqWordsMismatch('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC',10,2)
        
#freqWordsMismatch('CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT',9,3)
