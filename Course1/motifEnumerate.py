#!/usr/bin/env python
#########Motif Enumeration Problem##########
from dNeighbours import neighbors
from hamming import hamming_distance
import sys
def motifEnumerate(dna,k,d):
    seq_first=dna[0]
    patterns=[]
    l=len(seq_first)
    for i in xrange(l-k+1):
        patterns.append(seq_first[i:i+k])
    patterns=list(set(patterns))#unique patterns in the first string in DNA
    d_neighbor=[]
    for pattern in patterns:
        d_neighbor.extend(neighbors(pattern,d))
    d_neighbor=list(set(d_neighbor))#collection of unique d_neighbor for All kmer pattern from first string
#######Checking if d_neighbor pattern has a match in REST of dna collection of sequences##########    
    motif=[]
    for patt in d_neighbor:
        s=0
        for seq in dna[1:]:
            c=0
            for i in xrange(l-k+1):
                if hamming_distance(patt,seq[i:i+k])<=d:
                    c=1
                    s=s+1
                    break
                else:
                    pass
            if c==0:#that is patt never exists as a d-neighbor of patterns of an encountered seq! then NO NEED TO CHECK FOR SUBSEQUENT Sequences!
                break
            elif s==len(dna)-1:
                motif.append(patt)
    motif=list(set(motif))
    return motif
                
#dna=['ATTTGGC','TGCCTTA','CGGTATC','GAAAATT']
#dna=['TCTGAGCTTGCGTTATTTTTAGACC','GTTTGACGGGAACCCGACGCCTATA','TTTTAGATTTCCTCAGTCCACTATA','CTTACAATTTCGTTATTTATCTAAT','CAGTAGGAATAGCCACTTTGTTGTA','AAATCCATTAAGGAAAGACGACCGT']

dna=['CGTCCAGAATGGGTCCAAAACCGTC','CGTTATGCGAAGTCCCGTGATGGTG','CGTAGTTCAAGGCTCGATTCCAGGC','TCTGCTCAACCGTCTCTACGGACCC','GTACTCGTCCGTTTATGGGCTTTAC','CTTGGGGCGTCGTTGTTTCGGCTGG']
motifs=motifEnumerate(dna,k=5,d=2)
             
for motif in motifs:
    print motif,
