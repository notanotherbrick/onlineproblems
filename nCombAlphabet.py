# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 12:57:27 2016

@author: Hobbiton
"""

def nCombDP(i):
    if nums[i] == 0:
        return 0
    if i >=len(nums) - 1:
        return 1
    if dp[i] != -2 :
        return dp[i]
    
    res=0
    first = nCombDP(i+1)
    if first != 0:
        res += nCombDP(i+1)
    
    if i + 1 < len(nums) and 10* nums[i] + nums[i+1] <= 26:
        second = nCombDP (i+2) 
        if second != 0: 
            res += second
            
    dp[i] = res
    
    return res
    '''
def nComb(nums):
    if not nums:
        return 1
    if nums[0] == 0:
        return -1
    if len(nums) == 1:
        return 1
    
    res=0
    first = nComb(nums[1:])
    if first != -1:
        res += nComb(nums[1:])
    
    if len(nums)>1 and 10* nums[0] + nums[1] <= 26:
        second = nComb (nums[2:]) 
        if second != -1: 
            res += second
    
    return res
    
    '''
    
from random import randint
import time 

import numpy as np 

slope = [1] * 20




for i in xrange(1, 20):
    
    stime = time.time()
    dp = [-2]*(5**i)   
    dp[-1] = 1
    nums = [randint(0,9) for _ in xrange(5**i)]
    nCombDP(0)
    end_time = time.time()    

    slope[i] = end_time - stime
    print i , end_time - stime,
    if slope[i-1] > 0:
        print slope[i]/slope[i-1]
    
print 'slope', np.mean(slope)
print 'standard deviation', np.std(slope)    