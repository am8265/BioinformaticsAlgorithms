#!/usr/bin/env python
import math
def next_pattern(pattern,number):
    base_conv={'A':'C','C':'G','G':'T','T':'A'}
    for step in range(number):
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
def mod_pattern(pattern,k):
    base_next={'A':'C','C':'G','G':'T','T':'A'}
    for i in xrange(-1,-k-1,-1):
        if pattern[i]=='T':
            continue
        else:
            break
    if i==-1:#if the pattern's last character is not T!
        return (pattern,0)
    else:
        pattern=pattern[:k+i]+base_next[pattern[i]]+'A'*(-1-i)
        return (pattern,1)
    

def number_pattern(number,k):
    #base_next={'A':'C','C':'G','G':'T','T':'A'}
    pattern='A'*k
    if number==0:return pattern;
    index=number+1
    n=int(math.log(index,4))
    index_scan=1
    while n>=1:
        pattern=pattern[:k-n]+'T'*n
        index_scan+=(4**n)-1
        if index_scan<index:
            pattern,step=mod_pattern(pattern,k)
            index_scan+=step
            d=index-index_scan+1
            n=int(math.log(d,4))
        else:
            break
    else:
        pattern=next_pattern(pattern,d-1)

    return pattern
#print number_pattern(7733,9)



###Cycle-upto position####
#number=int(raw_input('Number:\n'))
#k=int(raw_input('Kmer:\n'))
#def cycle_position(number,k):
#    index_final=number+1#user input number 

#    steps=[]
#    index_diff=index_final#index_diff is initialized to index_final #take only the integer part
##    next=0#next is 0 unless incremented to 1,2 or 3
#    while index_diff>=4:#when this false
#        n=int(math.log(index_diff,4))
#        steps.append(n)
#        index_diff=index_diff-(4**n)+1
#    else:
#        next=index_diff-1
