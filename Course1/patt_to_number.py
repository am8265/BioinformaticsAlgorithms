#!/usr/bin/env python
def pattern_to_number(pattern):
    base_score={'A':0,'C':1,'G':2,'T':3}
    k=len(pattern)
    patt_number=0
    c=1
    for base in pattern:
        patt_number+=base_score[base]*(4**(k-c))
        c+=1
    return patt_number
#pattern=raw_input("Enter a pattern: \n")
#print pattern_to_number(pattern)
