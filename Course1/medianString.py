#!/usr/bin/env python
import sys
#######Solving the median string problem##########
from hamming import hamming_distance
from number_to_pattern import number_pattern
#########The h_dis function computes HAMMING DISTANCE b/w kmer pattern and All KMER PATTERNS IN A LARGER SEQUENCE & returns those kmer patterns with least HD with provided pattern######
def h_dis(pattern,seq):
    k=len(pattern)
    kmer_distance=dict()#kmer and HD 
    for i in xrange(len(seq)-k+1):
        kmer=seq[i:i+k]
        kmer_distance[kmer]=hamming_distance(pattern,kmer)#for all kmers in seq compute HD with pattern provided
    kmer_dist=kmer_distance.items()
    kmer_dist=sorted(kmer_dist,key=lambda x:x[1])
    smallest_hd=kmer_dist[0][1]
    kmer_dist_leastHD=[kmer_dist[0]]
    for k,v in kmer_dist[1:]:
        if v==smallest_hd:
            kmer_dist_leastHD.append((k,v))
        else:
            break
    return kmer_dist_leastHD# return type is a tuple of form (KMER,leastHD)
def pattern_gen(k):
    base_conv={'A':'C','C':'G','G':'T','T':'A'}
    pattern='A'*k
    patterns=[]
    patterns.append(pattern)                                                                                                                                                                   
    for i in xrange(1,4**k):
        c=0
        for pos in xrange(-1,-k-1,-1):
            if pattern[pos]!='T' and c==0:
                pattern=pattern[:k+pos]+base_conv[pattern[pos]]
                patterns.append(pattern)
                break
            elif pattern[pos]!='T' and c!=0:
                pattern=pattern[:len(pattern)+pos]+base_conv[pattern[pos]]+'A'*((-1*(pos+1)))
                patterns.append(pattern)
                break
            else:
                c=c+1
                continue
    return patterns
        
def medianString(dna,k):
    patt_dis=dict()#pattern to Hamming distance
    #########all kmers- USUAL population is 4**k kmers But not realistically possible for collection of "all kmers in Dna"
#    for pattern in pattern_gen(k):
    dis=0
    for seq in dna:# for every sequence in dna collection of sequences Compute "minimum HD between pattern and sequence"
        ham_dis=h_dis(pattern,seq)
            #print ham_dis
        dis=dis+ham_dis[0][1]#we are only interested in least HD and not the kmer  
    print dis
    patt_dis[pattern]=dis#####we compute the score(Motif) and assign for median pattern
    ####sorting for median string#######
    patt_dis=sorted(patt_dis.items(),key=lambda x:x[1])
    min_score=patt_dis[0][1]
    medianPattern=[patt_dis[0]]
    for k,v in patt_dis[1:]:
        if v==min_score:
            medianPattern.append((k,v))
        else:
            break
    return medianPattern#returns median String(s) with minimum score(Motifs) in Dna

#########We Test Code Here!###################################

#dna=['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTTCGGGACAG']
#print medianString(dna,3)[0][0]

fh=open(sys.argv[1])

#dna=['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC','GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC','GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']
#k=7
#dna=[]
for line in fh:
    dna=line.split(' ')
dna[-1]=dna[-1].strip('\n').strip('\r')
print dna

#seq=''
#j=0
#for c in line:
#    j+=1
#    seq=seq+c
#    if j%97==0:
#        dna.append(seq)
#        seq=''
#print dna
fh.close()
#print medianString(dna,k)
pattern='GGCCC'
#seq=['TTACCTTAAC','GATATCTGTC','ACGGCGTTCG','CCCTAAAGAG','CGTCAGAGGT']
#print dna
print medianString(dna,pattern)
