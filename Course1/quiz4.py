#!/usr/bin/env python
#genome=raw_input("Enter the sequence")
with open('rosalind.txt','r') as fh:
    genome=''
    while True:
        genome=genome+fh.readline()
        if fh.readline()=='':
            break
    fh.close()
skew=[0]*(len(genome)+1)
values=[0]
pos_skew=[(0,skew[0])]
for i in xrange(len(genome)):
    if genome[i].upper()=='C':
        values.append(-1)
    elif genome[i].upper()=='G':
        values.append(1)
    else:
        values.append(0)
    skew[i+1]=sum(values)
    pos_skew.append((i+1,skew[i+1]))
#print "skew:",skew
#print "Pos_skew:",pos_skew
print "Pos_Skew_Sorted:",sorted(pos_skew,key=lambda x:x[1])
