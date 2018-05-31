#!/usr/bin/env python
#####Find the revese complement of a string#############
import re
import sys
def revComplement(text):
    transcrTable={'A':'T','T':'A','G':'C','C':'G'}
    revComp=''
    for nuc in text:
        revComp=transcrTable[nuc]+revComp
    return revComp
#transcrTable={'A':'T','T':'A','G':'C','C':'G'}
#text=''
#fh=open(sys.argv[1],'r')
#for line in fh:
#    line=line.rstrip('\n').strip('')
#    line=line.upper()
    #if len(re.findall('[^ATG]+',line))<1:#if the lines DO NOT CONTAIN 1 or more non ATGC characters accept it!  
#    text=text+line
    #else:
    #    pass
    #print line
#print len(text)
#print revComplement(text,transcrTable)
