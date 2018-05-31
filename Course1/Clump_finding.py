#!/usr/bin/env python
from number_to_pattern import number_pattern
import sys
k=int(raw_input("K-mer:\n"))
#k=5
def pattern_to_number(pattern):
    k=len(pattern)
    base_order={'A':0,'C':1,'G':2,'T':3}
    pattern_ct=0
    for i in xrange(k):
        pattern_ct+=base_order[pattern[i]]*(4**(k-i-1))
    return pattern_ct

def clump_array(k,t,freq_array,clump=[0]*(4**k)):
    '''k-k value for k-mer pattern, t-minimum frequency of K-mer,freq-array-frequency Array of K-mer pattern/Window,clump-FrequencyArray of k-mer pattern forming clumps in that window,deafault initialises to all ZEROS'''
    for i in xrange(4**k):
        if freq_array[i]>=t:#If a k-mer pattern occurs atleast t times 
            clump[i]=1#Update clump as k-mer pattern forming clump
    return clump

genome=''
fh=open(sys.argv[1],'r')
for line in fh:
    line=line.rstrip().rstrip('')
    genome=genome+line
fh.close()
print genome
genome_len=len(genome)
#genome='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
##Ask for Window (L)Length, k(kmer value), t(maximal frequency) from the user
#L=50
L=int(raw_input("Window Size:\n"))
#k=int(raw_input("K-mer:\n"))
#t=4
t=int(raw_input("Frequency:\n"))
freq_array=[0]*(4**k)
#######Computing Freq array for k-mers in WINDOW 1#############
for i in xrange(L-k+1):#For a window slided once, collect all k mer patterns
    pattern=genome[i:i+k]
    index=pattern_to_number(pattern)
    freq_array[index]+=1

clump_first=clump_array(k,t,freq_array)#Clump First are the clumps forming in 1st WINDOW
##Conver the number to K-pattern forming Clumps!
#for i in xrange(4**k):
#    if clump_first[i]==1:
#        pattern_in_clump=number_pattern(i,k)
#        print pattern_in_clump

######This section efficiently computes Freq array for Window 2 onwards....
for i in xrange(1,genome_len-L+1):#every single iteration is a different  window...NOTE WE START AT 2nd Window!
    ##########Note: We have already made frequencyArray based on kmers in FIRST WINDOW..Hence forth we will ADD FIRST & LAST K-MER taken from WINDOW 2 ONWARDS...
    index_first=pattern_to_number(genome[i-1:i-1+k])#FIRST K-mer in previous window
    freq_array[index_first]-=1#update freq_array for each window, by deleting the COUNT OF FIRST KMER in PREVIOUS WINDOW!
    index_last=pattern_to_number(genome[i+L-k:i+L])#add a NEW-Kmer to the Frequency array FROM LAST K-Mer OF PRESENT WINDOW!

    freq_array[index_last]+=1# update freq_array FOR THE LAST WINDOW 
    clump=clump_array(k,t,freq_array,clump_first)#update clump for WINDOW 2 ONWARDS.....The final clump result will have 'ALL CLUMPS IN ALL WINDOWS!'
    
for i in xrange(4**k):
    if clump[i]==1:
        pattern_in_clump=number_pattern(i,k)
        print pattern_in_clump, 

