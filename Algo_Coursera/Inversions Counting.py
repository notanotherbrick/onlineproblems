# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:28:22 2015

@author: Gondor
"""

L=[int(line.rstrip('\n')) for line in open('IntegerArray-InversionCounting.txt')]

def countInversions(L,left,right):
    if (right-left==0):
        return 0
    mid=int((left+right)/2)
    x=countInversions(L,left,mid)
    y=countInversions(L,mid+1,right)
    z=countCrossInversions(L,left,mid,right)    
    return x+y+z

def countCrossInversions(L,left,mid,right):
 
    i=left
    j=mid+1
    inv=0
    k=0
    S=[0]*(right-left+1)
    #print "Left",left,"right",right,"Mid",mid,"List",L[left:right+1],"K :", k
    while(k<=(right-left)):
        #print S, "I is" , i , "J is :",j
        if(i>mid):
            S[k]=L[j]
            j+=1
        elif (j>right):
            S[k]=L[i]
            i+=1
        elif (L[i]<=L[j]):
            S[k]=L[i]
            i+=1
        else:
            inv+=mid-i+1
            S[k]=L[j]
            j+=1

            
        k=k+1
        
#        print "Inv is : ", inv
    #print L,S
    L[left:right+1]=S
    #print inv
    
    return inv

#L=[1,2,3,4,5,10,6,7,9]#,6,7]#3,5,8,9,2,4,6]
print countInversions(L,0,len(L)-1)
#print countCrossInversions(L,0,int((0+len(L)-1)/2),len(L)-1)