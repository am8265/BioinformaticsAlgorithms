#!/usr/bin/env python
import random
import re
import sys
from profile_kmer import profile_kmer
from greedyMotifPseudo import score,profile

def randomMotifs(dna,k,t):
    motifs=['TGA','GTT','GAA','TGT']
    profile_motif=profile(motifs,t)
    profile_mat=profile_motif[1]
    print profile_mat
    profile_prob=profile_motif[0]
    print profile_prob
    motifs_next=[]
    for seq in dna:
        motifs_next.append(profile_kmer(seq,k,profile_prob)[0])
    return motifs_next

dna=['TGACGTTC','TAAGAGTT','GGACGAAA','CTGTTCGC']
k=3
t=4
print randomMotifs(dna,k,t)
