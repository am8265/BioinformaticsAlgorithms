#!/usr/bin/env python
import profile_kmer
def score(update_profile,t):
    '''computes the score of a collection of motifs-Motifs'''
    #Call the hamming distance function to compute the score
    score=0
    for i in xrange(k):
        c=0
        for j in xrange(4):
            if update_profile.values()[j][i]==5:
                c=c+1
            if update_profile.values()[j][i]<=5 and c==2:
                score+=update_profile.values()[j][i]
    return score
                
def compute_profile(motif,k,profile):
    for i in xrange(k):
        for base in motif:
            profile[base][i]=profile[base][i]+1
    return profile

def prob_score(profile,k):
    prob_score={'A':[0]*k,'C':[0]*k,'G':[0]*k,'T':[0]*k}
    for base in prob_score.keys():
        for i in xrange(k):
            prob_score[base][i]=profile[base][i]/(profile['A'][i]+profile['C'][i]+profile['G'][i]+profile['T'][i])
    return prob_score
        
def greedy_motif_search(dna,k,t):
    motif_first=[]
    motifs_and_score=[]
    for i in xrange(len(dna[0])-k+1):
        motif_first.append(dna[0][i:i+k])
        
    base=['A','C','G','T']
    profile={'A':[0]*k,'C':[0]*k,'G':[0]*k,'T':[0]*k}
    for motif_1 in motif_first:
        motif_collection=[motif_1]
        update_profile=compute_profile(motif_1,k,profile)
        prob_score_update=prob_score(update_profile,k)
        for text in dna[1:]:
            profile_prob_motif,_=profile_kmer.profile_kmer(text,k,prob_score_update)#gets a profile most probable k-mer motif_next from text
            update_profile=compute_profile(profile_prob_motif,k,update_profile)# we update the profile for the motif_next passed
            prob_score_update=prob_score(update_profile,k)#update the prob_score for the profile now generated
            motif_collection.append(profile_prob_motif)#add the k-mer motif_next to the motif_collection
        print motif_collection
        motifs_and_score.append((motif_collection,score(update_profile,t)))
    motifs_and_score=sorted(motifs_and_score,key=lambda x:x[1])# lowest score motifs we will choose    
    return motifs_and_score[0]
fh=open('dna.txt','r')
dna=[]
for line in fh:
    dna.append(line.rstrip('\n').rstrip())
fh.close()
dna.pop()
print dna
t=len(dna)
print t
k=3
print greedy_motif_search(dna,k,t)
