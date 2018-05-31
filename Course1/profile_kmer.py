#!/usr/bin/env python
import re
import sys
def profile_kmer(text,k,profile):#profile could be passed as list(list of paired tuples or list of lists, dictionary
    '''takes in text,k value and profile(4*k) and returns most probable k-mer pattern(s) from the text'''
    prob_min=-1#minimum probability to compare with
    for i in xrange(len(text)-k+1):
        pattern=text[i:i+k]
        j=-1
        prob_score=1#initialzed prob_score to get the final value
        for base in pattern:
            j+=1
            prob_score=prob_score*float(profile[base][j])#computing probabilites of the k mer pattern
        if prob_score>prob_min:#as long as this condition is true we keep updating the prob_score and pattern(prob_pattern with highest probability is chosen) 
            prob_min=prob_score
            profile_prob_pattern=pattern
        else:
            pass
    return profile_prob_pattern,prob_min

#fh=open(sys.argv[1],'r')
#base=['A','C','G','T']
#c=-1
#text=''
#profile={}
#for line in fh:#please consider the last line
#    line=line.strip().rstrip('')
#    if re.search('[ACGT]+',line)!=None:
#        text=text+line
#    elif re.search('^[1-9]',line)!=None:
#        k=int(line)
#    else:
#        c=c+1
#        profile[base[c]]=line.split(' ')
#fh.close()
#print profile_kmer(text,k,profile)
#    profile[base[j]]=line.rstrip('\n').rstrip().split(' ')#profile={'A':[.......],'C':[.....]
#fh.close()    







#print profile#debug
#print profile_kmer('TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA',6,profile)
