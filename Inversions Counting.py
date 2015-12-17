# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:28:22 2015

@author: Gondor
"""

def countInversions(L,left,right):
    if (right-left==1) :
        return int(L[left]>L[right])
    if (right-left==0):
        return 0
    mid=int((left+right)/2)
    x=countInversions(L,left,mid)
    y=countInversions(L,mid+1,right)
    z=countCrossInversions(L,left,mid,right)    
    return x+y+z

def countCrossInversions(L,left,mid,right):
    

