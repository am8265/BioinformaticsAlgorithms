#!/usr/bin/env python
def count(seq,sub):
    '''Count function takes in a seq----sequence and sub---substring and returns the the count of the substring in the sequence.'''
    c=seq.find(sub)
    locate=[]#stores the position of 'sub' in 'seq'
    while c!=-1:#as long as a position is found or we have exhausted all positions
        locate.append(c)
        print c,
        c=seq.find(sub,c+1)#start searching the next position
        
    return len(locate)#length of the 'locate' provides u all such positions

def nmer(seq,n):
    '''for seq-sequence and n-kmer provided this function will return a sorted list of frequencies of the count of the k-mers in the sequence provided''' 
    nmer=set()
    nmer_count=[]
    for i in xrange(len(seq)-n+1):#all alignment positions
        nmer.add(seq[i:i+n])#a set of non-redundant 3-mers
    for mers in nmer:
        nmer_count.append((mers,count(seq,mers)))# nmer_count is a list of (nmers,count)tuples
    #we sort the list of (nmer,count) tuples based increasing count
    nmer_count=sorted(nmer_count,key=lambda x:x[1])
    return nmer_count#Its possible we may have >1 most/least frequent nmers
def rev_complement(seq):
    '''function returns the reverse complement of a string provided...eg. rev_complement('AAATC')--->('GATTT')'''
    rep={'A':'T','T':'A','G':'C','C':'G'}
    t=''
    seq=seq.upper()
    for nu in seq:
        t=rep.get(nu,'N')+t#reverse complement.. note that empty string 't' appears later
    return t
import getopt
import sys
def usage():
    """show the usage of the script"""
    print """./quiz1.py -n <kmers> -h
-n <Provide the kemers such as 3,5 ..upto maximum length of sequence>

-h <help for options>

-i <input file----optional>

-o <output file>
"""

o,k=getopt.getopt(sys.argv[1:],'n:i:o:h')
o=dict(o)
if o.get('-h',0)!=0:#if True means user has entered the '-h' option
    usage();sys.exit(0)#call usage and exit out 
#else:
#    usage();sys.exit("Please Provide a valid argument as explained in the help# file!")
if o.get('-n',0)>=1:#we expect that the n-value is atleast 1(1mer,2 mers..etc)
    n=int(o['-n'])# nmer value
else:
    usage();sys.exit("Please Provide atleast a valid  <kmer>!")#if '-h' and '-n'(with valid options) is not provided inform the user about the choices and exit out 
if o.get('-i','NA')=='NA':#if user doesn't enter input file we assume that it will be entered as RAWInput 
    seq=raw_input('Enter a Sequence:')
else:#if the user has provided a file name lets do some error handling
    try:# check if the file exist
        fh_i=open(o.get('-i'),'r')
    except:#if file doesn't exist show usage and ask the user to provide a valid file name withour raising an exception
        usage();sys.exit("Please Enter a valid file name (with correct relative/absoulte path to continue")
    else:#lets read the file..if the file exists
        seq=''
        while True:
            line=fh_i.readline().rstrip()
            seq=seq+line
            if line=='':#i.e if we reach end of the file
                break
        fh_i.close()    
            
#seq=raw_input('Enter a Sequence:')
print (nmer(seq,n))#both cases we output nmers on standard I/O terminal
if o.get('-o','NA')!='NA':#if -o argument is provided
    try:
        fh=open(o.get('-o'),'w')
    except:
        usage();sys.exit(0)
    else:
        seq_rcomp=rev_complement(seq)
        i=0
        #while seq_rcomp[i:i+80]!='':
            #fh.write(seq_rcomp[i:i+80]+'\n')
            #i=i+80
        fh.write(seq_rcomp)
        fh.close()
print ('Rev Complement:%s'%(rev_complement(seq)))
#fh.write(complement(seq))
#fh.close()
#print (nmer(seq,n)+'\n'+"RevComplemet for the string entered is:%s"%(complement(seq))
#print ("RevComplemet for the string entered is:%s"%(complement(seq))
