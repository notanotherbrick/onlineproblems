# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 20:41:35 2016

@author: Hobbiton

"""



def student_shuffle(A):
    if not A:
       return 0
    A_sorted=sorted(A)
    
    i=0
    while i<len(A) and A[i]==A_sorted[i]:
        i+=1
    
    if i==len(A):
        return 0
    
    start=i-1
    i=len(A)-1
    
    while i>0 and A[i]==A_sorted[i]:
        i-=1
    
    end=i+1
    
    return end-start-1
    


print student_shuffle([8,4,1,1,1,2,4,5,6,7,8,9])