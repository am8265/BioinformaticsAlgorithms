#!/usr/bin/env python
import re
import sys
from numpy.random import choice
nuc_length=int(sys.argv[1])
seq=''
for i in xrange(nuc_length):
    seq+=choice(['A','T','G','C'])
print seq
