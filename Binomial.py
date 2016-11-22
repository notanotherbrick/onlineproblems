# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 16:33:58 2016

@author: Hobbiton
"""


def solution(N, K):
    # write your code in Python 2.7
    if K>N:
        return -1
    
    
    
    res=1L
    
    K=min(K,N-K)
    
    for i in xrange(1,K+1):
        res*=(N-i+1)/float(i)        
        if res>1000000000:
            return -1
        
    return int(res)

import math
print (solution(98,6),10)