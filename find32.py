# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:14:49 2016

@author: Hobbiton
"""

def find32(L):
    i=len(L)-1
    
    lar=L[i]
    mid=-float('inf')    
    while(i>=0):
        if L[i]>lar:
            mid,lar=lar,L[i]
            print i,mid,lar
            return
        elif mid==-float('inf'):
            lar=min(lar,L[i])
        i-=1
        
find32( [5,1,2,3,5,6,7,8])