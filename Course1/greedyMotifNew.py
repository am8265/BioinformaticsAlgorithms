#!/usr/bin/env python
import sys
import re
def score(profile):
   score=0
   for i in xrange(len(profile.values()[0])):
      count=[]
      for cts in profile.values():
         count.append(cts[i])
      count.sort()
      score+=sum(count[:len(count)-1])
   return score
         
def profile(motifs,t):
    '''motifs-collection of kmer pattern provided as a list
    returns the profile matrix'''
    k=len(motifs[0])
    t=float(t)
    profile={'A':[0]*k,'C':[0]*k,'G':[0]*k,'T':[0]*k}
    for motif in motifs:
        i=-1
        for nuc in motif:
            i=i+1
            profile[nuc][i]+=1
    #print profile
    profile_prob={'A':[ct/t for ct in profile['A']],'C':[ct/t for ct in profile['C']],'G':[ct/t for ct in profile['G']],'T':[ct/t for ct in profile['T']]}
    return (profile_prob,profile)

def greedyMotif(dna,k,t):
    l=len(dna[0])#length of first/ALL sequence
    max_score=t*len(dna[0])#if ALL are small
    motifs_to_score={}
    #motifs=[]#Motif collection-Motifs
    for i in xrange(l-k+1):#indexing kmer Motif in FIRST sequence of DNA
       motifs=[]#Motif collection-Motifs
       motif1=dna[0][i:i+k]#kmer Motif1 in DNA1
       motifs.append(motif1)
#      motifs_profile_prob=profile(motifs)[0]#get only the profile_prob of motifs formed
       for seq in dna[1:]:#DNA2 onwards we select for kmer Motif2.... based on Motifs1 from DNA1
          motifs_profile_prob=profile(motifs,t)[0]#get only the profile_prob of motifs formed
          profile_probMotif={}
          for i in xrange(l-k+1):#kmer motif2 .....from DNA2....
             j=-1
             prob_of_motif=1
             for nuc in seq[i:i+k]:
                j=j+1
                prob_of_motif=prob_of_motif*motifs_profile_prob[nuc][j]#Compute profile-probability Kmer 
             profile_probMotif[i]=prob_of_motif# for Motif2...(stored as index)...store probability fo that motif
          profile_probMotif=sorted(profile_probMotif.items(),key=lambda x:(x[1],x[0]))#Sort from low to high probability of kmer in Motif2...and select
          prob_high=profile_probMotif[-1][1]#Highest probability among all motifs
          for indx,pr in profile_probMotif:
             if pr==prob_high:#the earliest index at which probability is highest
                break
             else:
                pass
          profile_kmer=seq[indx:indx+k]#find the kmer Motif which has is profile-most probable kmer
          motifs.append(profile_kmer)#add it to motifs
#######Selecting for Best Scoring Motifs######################
       motif_score=score(profile(motifs,t)[1])
       if motif_score<=max_score:
          best_motif=motifs
          max_score=motif_score
    return best_motif
          
###########Testing###############

#dna=['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']
#k=3
#t=5
    
#print greedyMotif(dna,k,t)
#fh=open(sys.argv[1])
#text=[]
#for line in fh:#please consider the last line                                     
#   line=line.strip().rstrip('')
#   if re.search('^[1-9]',line)!=None:
#      k,t=line.split(' ')
#      k=int(k)
#      t=float(t)
#   elif re.search('[ACGT]+',line)!=None:
#      text.append(line)
#fh.close()
#bestmotif=greedyMotif(text,k,t)
#for motifs in bestmotif:
#   print motifs
