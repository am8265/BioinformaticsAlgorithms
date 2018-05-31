#!/usr/bin/env python
#Text=raw_input("Enter Seq:")
Pattern=raw_input("Enter Pattern")
d=raw_input("No. of mismatches")
Text=''
with open('rosalind.txt') as fh:
    while True:
        Text+=fh.readline().rstrip()
        if fh.readline().rstrip()=='':
            break# we have reached the end of file/EOF
    fh.close()
    
pos=[]
for i in xrange(len(Text)-len(Pattern)+1):
    c=0
    for ind in xrange(len(Pattern)):
        if Text[i:i+len(Pattern)][ind]!=Pattern[ind]:
            c=c+1
            if c>int(d):
                match=False
                break
        else:
            match=True
    if match==True:pos.append(i)
fh=open('out.txt','w')
for positions in pos:
    print positions,
    fh.write(str(positions)+' ')
fh.close()
