#!/usr/bin/env python
'''This module computes the k-mer median string for a collection of dna strings based on minimization of score(Motifs)''' 
#import number_to_pattern
import hamming
def d(pattern,dna):
    '''function takes in pattern and collection of strings dna and computes thelowest  distance between the pattern and collection '''
    k=len(pattern)
    #distance=k#maximum possible hamming distance between pattern and region of same length
    total_hd=0
    for region in dna:
        distance=k+1
        #print region
        for i in xrange(len(region)-k+1):#for every region we compute the hamm distance between pattern and substrings of region and selct the substring with least distance 
            hd=hamming.hamming_distance(pattern,region[i:i+k])
            if distance>hd:
                distance=hd#we only keep the lowest hamming distance
        #print distance
        total_hd+=distance#sum of the least distances are computed for ALL REGIONS in dna for the PATTERN provided
    #print 'total_hd',total_hd,pattern
    return total_hd
                  
                                                        
                                                           

def median_string(dna,k):
    '''dna-collection of sequences/regions and k - kmer value/length--for these two input values the function returns a median string'''
    #distance=k*len(dna)#initialized distance=k*len(dna)i.e maximum value of sum_d
    base_conv={'A':'C','C':'G','G':'T','T':'A'}
    pattern='A'*k#Initial pattern
    #hamm_distance=[]
    #if distance>=d(pattern,dna):
    #        distance=d(pattern,dna)
    #        median_pattern=pattern#median_pattern gets updated
    
    #print pattern
    hamm_distance=[(pattern,d(pattern,dna))]#[(pattern,leastHD).....]
    for i in xrange(1,4**k):#Searching the kmer pattern SPACE!
        c=0
        for pos in xrange(-1,-k-1,-1):
            if pattern[pos]!='T' and c==0:
                pattern=pattern[:k+pos]+base_conv[pattern[pos]]
#                print pattern
                break
            elif pattern[pos]!='T' and c!=0:
                pattern=pattern[:len(pattern)+pos]+base_conv[pattern[pos]]+'A'*((-1*(pos+1)))
#                print pattern
                break
            else:
                c=c+1
                continue

        #pattern=number_to_pattern.number_pattern(i,k)
        #distance=k*len(dna)#initialized distance=k*len(dna)i.e maximum value of sum_d
        #if distance>=d(pattern,dna):
        #    distance=d(pattern,dna)
        #    median_pattern=pattern#median_pattern gets updated
        hamm_distance.append((pattern,d(pattern,dna)))
    hamm_distance=sorted(hamm_distance,key=lambda x:x[1])#sorting based on least hamming distance!...low to High
    #return median_pattern
    return hamm_distance#return the sorted hamm_distance
#fh=open('dna.txt','r')
dna=['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC','GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC','GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']
#for line in fh:
#    dna.append(line.rstrip('\n').strip(' '))
#fh.close()

#print dna
med_string= median_string(dna,7)
for i in med_string:
    print i
