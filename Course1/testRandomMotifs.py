#!/usr/bin/env python
from profile_kmer import profile_kmer
from greedyMotifPseudo import score,profile
egmotifs=['GTC','CCC','ATA','GCT']
dna=['ATGAGGTC','GCCCTAGA','AAATAGAT','TTGTGCTA']
k=3
profile_motif=profile(egmotifs,t=4)#Random Motifs profile is computed!      
#print profile_motif
profile_matrix=profile_motif[1]
profile_prob=profile_motif[0]
#print profile_prob
score_motifs=score(profile_matrix)
c=0
for i in xrange(3):
    c+=1
    motifs_next=[]#initialise for next Set of motifs!                       
    for seq in dna:
        #print profile_prob
        motifs_next.append(profile_kmer(seq,k,profile_prob)[0])
    #print profile_kmer(seq,k,profile_prob)                            
    motifs=motifs_next
    print motifs
    profile_motif=profile(motifs,4)
    profile_matrix=profile_motif[1]
    profile_prob=profile_motif[0]

#print motifs
#print c
