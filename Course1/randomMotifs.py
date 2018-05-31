#!/usr/bin/env python
import timeit
import random
import re
import sys
from profile_kmer import profile_kmer
from greedyMotifPseudo import score,profile##### profile functions computes pseudo probability matrix
import time
#def profileMatrix(motifs):
#    base=['A','C','G','T']
#    c=-1
#    profile_matrix={'A'=0,'C'=0,'G'=0,'T'=0}
#    for motif in motifs:
#        for base in motif:
#            profile[base]+=1
#    return profile_matrix


def randomMotifSearch(dna,k,t):
####select Random Motifs from random kmers########
    motifs=[]
    l=len(dna[0])
    for seq in dna:
        i=random.randrange(0,l-k+1,1)#choosing indices/kmer motifs RANDOMLY!
        motifs.append(seq[i:i+k].upper())#i should be a random number from (0 to length(dna)-k)
    #profile_matrix=profileMatrix(motifs)
    #print motifs
    egmotifs=['TGA','GTT','GAA','TGT']
    
    profile_motif=profile(motifs,t)#Random Motifs profile is computed! 
    profile_matrix=profile_motif[1]#Raw profile of counts needed to compute Score(Motifs)
    #print profile_matrix
    profile_prob=profile_motif[0]#Profile_prob_based on Pseudo Counts
    #print profile_prob
    score_motifs=score(profile_matrix)#Score of profile matrix!
    #print score_motifs
    while True:
        motifs_next=[]#initialise for next Set of motifs!
        for seq in dna:
            motifs_next.append(profile_kmer(seq,k,profile_prob)[0])
            #print profile_kmer(seq,k,profile_prob)
        print motifs
        profile_motif=profile(motifs_next,t)#compute profile for MotifsNext!
        #print profile_motif
        profile_matrix=profile_motif[1]#profile matrix is NOT pseudo!
        profile_prob=profile_motif[0]#profile prob pseudo!
        score_motifs_next=score(profile_matrix)#score of the MotifNext
        #print score_motifs_next
        if score_motifs_next<score_motifs:#As long as we have Lower Scores...
            score_motifs=score_motifs_next
            motifs=motifs_next
        else:
            return motifs,score_motifs
#######deleting this codeFor now#############
#def randomMotif1000(dna,k,t,n=1000):
#    motifs,score_motifs=randomMotifSearch(dna,k,t)
#    for i in xrange(n-1):
#        if n==1:
#            break
#        motifs_next,score_motifs_next=randomMotifSearch(dna,k,t)
#        if score_motifs_next<score_motifs:
#            score_motifs=score_motifs_next
#            motifs=motifs_next
#        else:
#            pass
#    return motifs
#start=timeit.timeit()

#########Testing Code##################
#dna=['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA\
#dna=['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

#k=8
#t=5
#print randomMotif1000(dna,k,t)
#start=time.time()
#fh=open(sys.argv[1])
dna=['TGACGTTC','TAAGAGTT','GGACGAAA','CTGTTCGC']
#for line in fh:
#    line=line.strip().strip(' ')
#    dna.append(line)

k=3
t=4
randomMotifSearch(dna,k,t)




#fh.close()
#motifs=randomMotif(dna,k,t,n=2000)
#for i in xrange(len(motifs)):
#    print motifs[i]

#end=time.time()
#end=timeit.timeit()
#print (end-start)
