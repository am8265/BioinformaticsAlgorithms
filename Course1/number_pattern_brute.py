#!/usr/bin/env python
import math
def next_pattern(k):
    base_conv={'A':'C','C':'G','G':'T','T':'A'}
    pattern='A'*k
    print pattern
    for i in xrange(1,4**k):
        c=0
        for pos in xrange(-1,-k-1,-1):
            if pattern[pos]!='T' and c==0:
                pattern=pattern[:k+pos]+base_conv[pattern[pos]]
                print pattern
                break
            elif pattern[pos]!='T' and c!=0:
                pattern=pattern[:len(pattern)+pos]+base_conv[pattern[pos]]+'A'*((-1*(pos+1)))
                print pattern
                break
            else:
                c=c+1
                continue
        
next_pattern(5)
