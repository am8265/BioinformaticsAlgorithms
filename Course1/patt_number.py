#!/usr/bin/env python
'''This module has functions for converting a k-mer pattern to Number/lexicographic order &  also vice versa when a kmer value and lexicographic order is provided'''
#def pattern_to_number(pattern):
#    ''' A function that takes a give kmer 'Pattern' as an argument and returns the lexicographic order of the Pattern'''
#    lex_order=0
#    lex_score={'A':0,'T':3,'C':1,'G':2}
#    for order in pattern[-1::-1]:
#        lex_order=lex_order+lex_score[order.upper()]
#    return lex_order
#pattern=raw_input("Enter the k-mer Pattern:\n")
#print pattern_to_number(pattern)

#print number_to_pattern
import math
#def construct_pattern(pos_in_pattern,k):
#    '''function returns a  Pattern (with a particular lexicographic order  when pos_pattern list & length of pattern(k) is passed'''
#    pattern=['A']*k#intial starting Pattern of length k with lexicographic order 0
#    if pos_in_pattern[0]-1==0:
#        pattern=''.join(['T']*k)# returning the string 'TTTTTT...k'...if we get errors try
#        return pattern
#    else:
#        for pos in pos_in_pattern:# we continue iterating until we get the rough final pattern
#            pattern=pattern[:pos-1]+['C']+pattern[pos:]#AAAAcAAAA
#        return pattern

#def number_to_pattern(index,k):
#    '''returns a Pattern when a lexicographic order and the k-mer value is provided'''
    lex_rev_score={0:'A',1:'C',2:'G',3:'T'}
    c=index+1
    n=int(math.log(c,4))
    pos_in_pattern=[]
    while (c-(4**n))>=4:
        pos_in_pattern.append(k-n)
        c=c-(4**n)
        n=int(math.log(c,4))
    pattern=construct_pattern(pos_in_pattern,k)
    if c==0:# if we have reached end of pattern while comparing ..shift 1 step backwards
        #go 1 step backward
        pattern=''.join(pattern[:k-n-1]+['A']+['T']*len(k-pattern[:k-n]))
    else:
        offset=c-1
        print 'offset:',offset
        #pattern=''.join(pattern[:k-1]+[lex_rev_score[offset]])
        return pattern


def next_pattern(pattern,steps):
    base_conv={'A':'C','C':'G','G':'T','T':'A'}
    for step in range(steps):
        c=0
        for pos in xrange(-1,-len(pattern)-1,-1):
            if pattern[pos]!='T' and c==0:
                pattern=pattern[:len(pattern)+pos]+base_conv[pattern[pos]]
                break
            elif pattern[pos]!='T' and c!=0:
                pattern=pattern[:len(pattern)+pos]+base_conv[pattern[pos]]+'A'*((-1*(pos+1)))
                break
            else:
                c=c+1
                continue
    return pattern

pattern=raw_input("Enter a Pattern: ").upper()
steps=int(raw_input("Steps :"))


#index=int(raw_input('Enter index: \n'))
#k=int(raw_input('Enter k:\n'))
print next_pattern(pattern,steps)
#print number_to_pattern(index,k)
