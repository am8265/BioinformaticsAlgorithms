#!/usr/bin/env python
def Count(seq,sub):
    c=seq.find(sub)
    locate=[]
    while c!=-1:
        locate.append(c)
        c=seq.find(sub,c+1)
    return locate
 
#seq=raw_input("Enter Whole seq")
with open('rosalind.txt') as fh:
    seq=''
    while True:
        seq=seq+fh.readline()
        if fh.readline()=='':
            break# we have reached the end of file/EOF
    fh.close()

sub=raw_input("Enter sub")
locate=Count(seq,sub)
with open('out.txt','w') as fh:
    for i in locate:
        fh.write(str(i)+' ')
    fh.write('\n')
    fh.close()
#print locate    
