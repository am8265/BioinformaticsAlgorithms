#!/usr/bin/env python
from number_to_pattern import number_pattern
from freq_array import computing_freq
def FasterFrequentWords(text,k):
    freq_patterns=[]
    freq_array=computing_freq(text,k)
    maxCount=max(freq_array)
    for i in xrange(4**k):
        if freq_array[i]==maxCount:
            pattern=number_pattern(i,k)
            freq_patterns.append(pattern)
    return freq_patterns

    
