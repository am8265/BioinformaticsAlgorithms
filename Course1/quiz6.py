#!/usr/bin/env python
def Count(seq,sub):
    c=seq.find(sub)
    locate=[]
    while c!=-1:
        locate.append(c)
        c=seq.find(sub,c+1)
    return len(locate)

def nmer(seq,n):# function takes in sequence and n mer
    nmer=set()
    nmer_count=[]
    for i in xrange(len(seq)-n+1):#all alignment positions
        nmer.add(seq[i:i+n])# add all unique nmers
    for mers in nmer:
        nmer_count.append((mers,Count(seq,mers)))# have each nmer & count value respectively
    return nmer_count
def compare(nmerCount,d):
    kmer=dict()
    for i in xrange(len(nmerCount)):
        for j in xrange(i+1,len(nmerCount)):
            c=0;mismatch=[]
            for b_ind in xrange(len(nmerCount[i][0])):
                if nmerCount[i][0][b_ind]!=nmerCount[j][0][b_ind]:# i,j pairs are unique nmer pairs !
                    c=c+1
                    mismatch.append(b_ind)
                    if c>d:
                        match=False;break
                else:
                    match=True
            if match==True:kmer[(i,j)]=(mismatch,nmerCount[i][1]+nmerCount[j][1])#ind    
    return kmer                    
seq=raw_input("Seq:")
n=int(raw_input("kmer:"))
d=int(raw_input("d:"))
nmer_count=nmer(seq,n)
print len(nmer_count)
print nmer_count
print compare(nmer_count,d)
