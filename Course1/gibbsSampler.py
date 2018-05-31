#!/usr/bin/env python
#######Gibbs Sampler###########
import random
import re
import sys
#from profile_kmer import profile_kmer
#########Score Evaluation could be changed#######
from greedyMotifPseudo import score,profile
from numpy.random import choice

def randomGenerate(pattern_prob):#[(pattern,prob),.....]
    patterns=[x for x,v in pattern_prob]
    prob_dist=[v for x,v in pattern_prob]
    prob_dist2=[v/float(sum(prob_dist)) for v in prob_dist] 
#######choose either prob_dist or prob_dist2#############
    draw=choice(patterns,1,p=prob_dist2)
    #print prob_dist2
    return draw[0]

def profile_kmer(text,k,profile):#profile could be passed as list(list of paired tuples or list of lists, dictionary                                                               
    '''takes in text,k value and profile_probability(4*k) and returns most probable k-mer pattern(s) from the text'''
    #prob_min=-1#minimum probability to compare with
    pattern_prob={}
    #index_prob=[0]*(len(text)-k+1)#initialise for kmer indices
    for i in xrange(len(text)-k+1):#iterate over all kmers
        pattern=text[i:i+k]
        j=-1
        prob_score=1#initialzed prob_score to get the final value                                                                                                                  
        for base in pattern:#for each kmer!
            j+=1
            prob_score=prob_score*float(profile[base][j])#computing probabilites of the k mer pattern                                                                              
        #index_prob[i]=prob_score#probability scores for indices/kmers
        if pattern_prob.get(pattern,0)!=0:#if the kmer was counted before
                   pattern_prob[pattern]+=prob_score
        else:
           pattern_prob[pattern]=prob_score
#if prob_score>prob_min:#as long as this condition is true we keep updating the prob_score and pattern(prob_pattern with highest probability is chosen)                     
        #prob_min=prob_score
        #profile_prob_pattern=pattern
        #else:
        #pass
    #print index_prob.items()
    #index=randomGenerate(index_prob)
    random_kmer_motif=randomGenerate(pattern_prob.items())#[(pattern,probab)....]
    return random_kmer_motif
    #return text[index:index+k]#returning the Pattern

def gibbsSampler(dna,k,t,n):
    motifs=[]
    l=len(dna[0])
    #######creating First random Motifs#######
    for seq in dna:
        i=random.randrange(0,l-k+1,1)#select a random index/kmer
        motifs.append(seq[i:i+k])
    profile_motif=profile(motifs,t)
    profile_matrix=profile_motif[1]#profile_matrix with real counts!
    profile_prob=profile_motif[0]#profile_probability pseudo!
    score_motifs=score(profile_matrix)#score of this FIRST MOTIFS!
    #print motifs,score_motifs
    for j in xrange(n):#N Iterations
        i=random.randrange(0,t,1)# select the ith sequence from Dna of t sequences RANDOMLY! This would be deleted to create a PROFILE
        motifs_del=motifs
        del motifs_del[i]#motifs_del WITHOUT ith Motif
        profile_motif_del=profile(motifs_del,t-1)#profile_pseudo_prob and profile_countMatrix is returned for "Truncated Motifs"
        profile_mat_del=profile_motif_del[1]#Truncated Motifs -->Profile Matrix
        profile_prob_del=profile_motif_del[0]#Truncated Motifs--->Probability Pseudo Matrix
        random_motif=profile_kmer(dna[i],k,profile_prob_del)#for the ith sequence that was TRUNCATED compute the "Random kmerMotif" based on probability distribution of all kmers computed
        motifs_del.insert(i,random_motif)#a randomly generated motif -'randomPattern'  from ith seq in dna gets inserted and a New motif motifs_next forms
        motifs_next=motifs_del#This is a new motifs found after Gibbs sampling 
        #print motifs_next
        score_motifs_next=score(profile(motifs_next,t)[1])
        if score_motifs_next<score_motifs:
            score_motifs=score_motifs_next
            motifs=motifs_next
        else:
            motifs=motifs_next
    return motifs,score_motifs

##########Testing Code############
dna=['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

k=8
t=5
n=100
#dna=[]
#fh=open(sys.argv[1])
#for line in fh:
#    line=line.strip().rstrip(' ')
#    dna.append(line)
#fh.close()
#k=15
#t=20
#n=2000

motifs,score_motifs=gibbsSampler(dna,k,t,n)
print motifs,score_motifs
for i in xrange(1000):
    motifs_next,score_next=gibbsSampler(dna,k,t,n)
    print motifs_next,score_next
    if score_next<score_motifs:
        score_motifs=score_next
        motifs=motifs_next
    else:
        pass
    
for motif in motifs:
    print motif
        
