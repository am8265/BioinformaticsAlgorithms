#!/usr/bin/env python
def Count(seq,sub):
    c=seq.find(sub)
    locate=[]
    while c!=-1:
        locate.append(c)
        c=seq.find(sub,c+1)
    return len(locate)

def nmer(seq,n):# nmers 
    nmer=set()
    nmer_count=[]
    for i in xrange(len(seq)-n+1):#all alignment positions
        nmer.add(seq[i:i+n])
    return nmer
#    for mers in nmer:
#        nmer_count.append((mers,Count(seq,mers)))# nmer_count is a list of (nmers,count)tuples
    #we sort the list of (nmer,count) tuples based increasing count
#    nmer_count=sorted(nmer_count,key=lambda x:x[1])
#    return nmer_count

def window(seq,l,n):#seq-Genome seq and l-window/interval 
    lmer=[]
    kmer=nmer(seq,n)#Could be independently called / parallezed
    nmerCount_window={}
    for i in xrange(len(seq)-l+1):
        lmer.append(seq[i:i+l])
    for mers in kmer:# we scan every window out of all possible windows
        w_mers=[]
        for w in lmer:
            w_mers.append((w,Count(w,mers)))
            w_mers=sorted(w_mers,key=lambda x:x[1])
        nmerCount_window[mers]=w_mers
    return nmerCount_window
#seq=raw_input("Enter Genome seq:")
with open('rosalind.txt') as fh:
    seq=''
    while True:
        seq=seq+fh.readline()
        if fh.readline()=='':
            break# we have reached the end of file/EOF
    fh.close()
print "seq:",seq
l=int(raw_input("window length:"))
n=int(raw_input("nmer:"))
t=int(raw_input("min ocurence:"))
nmerCount_window=window(seq,l,n) 
for k in nmerCount_window.keys():
    if nmerCount_window[k][-1][1]>=t:
        print k
    else:
        pass
