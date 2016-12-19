# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:53:54 2016

@author: Hobbiton
"""
import collections
x=collections.defaultdict(list)

from random import randint

#A=[18, 3, 2, 11, 5, 3, 7, 16, 19, 5, 16, 14]

def median_of_medians(A,n,k):
    if not n:
        return
    if n<5: # base case
        return sorted(A)[k-1]
    C=[]
    for i in xrange(len(A)/5):
        C.append(median5(A[5*i:5*(i+1)]))
    # Handle edge case
    t=median5(A[5*(1+i):])
    if t:
        C.append(t)
    #print C

    p=median_of_medians(C,len(C),len(C)/2)
    #print p,k
    s,m,e=0,0,len(A)-1
    while(m<=e):
        if A[m]==p:
            m+=1
        elif A[m]<p:
            A[s],A[m]=A[m],A[s]
            s+=1
            m+=1
        else:
            A[e],A[m]=A[m],A[e]
            e-=1
            #A[e]=A[m]
    
    #print A,m
    
    if k==m:
        return p
    elif k<m:
        return median_of_medians(A[:m-1],m-1,k)
    else:
        return median_of_medians(A[m:],len(A[m:]),k-m)
    #print p,A
#            
            
    


def median5(A):
    if A:
        A.sort()
        return A[len(A)/2]
    
A=[0,0,0,0,0,0,1,1,1,1,0]
k=4
if not median_of_medians(A,len(A),k)==sorted(A)[k-1]:
        print A,k
#
#for _ in xrange(10000):
#    n=randint(10,100)
#    A=[randint(0,100) for _ in xrange(n)]
#    k = randint(1,n)
#    if not median_of_medians(A,len(A),k)==sorted(A)[k-1]:
#        print A,n,k
#        break
#    
