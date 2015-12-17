# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:31:45 2015

@author: Gondor
"""

L=[12,0,0,00,0,00,123,12,31,24,0,54,565,626056060,605,66,506,50,0,065,605,65,60,0,65,0,05,065,9590505,4650,20,150,05,5040,0,54,0,0,0,0,0,004,5,50,1,0,3,0,134,412,15]

def zeroTrail(L,start,end):
    if start==end:
        return
    
    zeroTrail(L,start+1,end)
  #  print L[start]
    if L[start]==0:
       # print "True",L[start:end]
        for i in range(s,e):
            L[i]=L[i+1]
            if L[i]==0:
                break


        L[e]=0
    
zeroTrail(L,0,len(L)-1)
#swapper(L)
print L      