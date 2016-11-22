# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:11:03 2016

@author: Hobbiton
"""
import random

median=13
L=[random.randint(0,23) for _ in xrange(32)]
print L
top,mid=0,0
bottom=len(L)-1
while mid<bottom: # check for termination
    if L[mid]<median: #bottom
        t=L[mid]       
        L[mid]=L[bottom]
        L[bottom]=t
        bottom-=1
    elif L[mid]>median:#top
        t=L[mid]        
        L[mid]=L[top]
        L[top]=t
        top+=1
        #print L[mid]
        mid+=1
    elif L[mid]==median:
        mid+=1

print L