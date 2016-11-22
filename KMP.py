# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:16:42 2016

@author: Hobbiton
"""



T="aaabbababbabbbabaaab"
P="abbabbbabaa"

def KMP(P,T):
    h=[-1]*(1+len(P))
    h[0]=-1
    
    P="$"+P
    for i in xrange(1,len(P)):
       #print i,P[i],h
        q=h[i-1]
        #print i
        h[i]=0
        while q>=0:
            if P[i]==P[q+1]:
                h[i]=q+1
                break
            q=h[q]
 
    i=0
    j=0
    P=P[1:]
    #h=h[1:]
    
    print h
    
    
    while i<len(T):

        if i<len(T) and T[i]==P[j]:
            print 'mmatch i = ',i,'j =',j, T[i],P[j]            
            i+=1
            j+=1
            if j==len(P):
                return i-j
        #print 'shift ->',h[j-1],i
        else: 
            j=h[j-1]
        #i+=j
        #print j
    
    return -1
print KMP(P,T)
print T.find(P)