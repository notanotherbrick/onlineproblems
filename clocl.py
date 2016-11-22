# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 20:00:44 2016

@author: Hobbiton
"""



def clock(A, B, C, D):
    # write your code in Python 2.7
    if A==None or B==None or C==None or D==None:
        return 'NOT POSSIBLE'
        
    nums=[A,B,C,D]
    
    hh_combinations=[]
    for i in xrange(4):
        for j in xrange(4):
            if i!=j:
                hh_combinations.append(str(nums[i])+str(nums[j]))
    
    
    hh='-1'
    for hh_candidate in hh_combinations:
        if int(hh_candidate)<24 and int(hh_candidate)>int(hh):
            hh=hh_candidate
    print hh
    if hh=='-1':
        return 'NOT POSSIBLE'
    
    
    nums.remove(int(hh[0]))
    nums.remove(int(hh[1]))
    
    mm_combinations=[str(nums[0])+str(nums[1]),str(nums[1])+str(nums[0])]
    
    mm='-1'
    for mm_candidate in mm_combinations:
        
        if int(mm_candidate)<60 and int(mm_candidate)>int(mm):
            mm=mm_candidate
    
    print mm,mm_combinations
    if mm=='-1':
        return 'NOT POSSIBLE'
 
    
    return  hh+" : "+mm
print clock(2,4,0,0)    