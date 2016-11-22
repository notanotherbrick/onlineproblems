# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 23:15:24 2016

@author: Gondor
"""
y=[[15, 76], [25, 0], [60, 91], [80, 0]]
z= [[70, 72], [90, 59], [120, 0]]


nz=len(z)
ny=len(y)
i=0
j=0
x=[]
cur=0
lastzh=0
lastyh=0

while(i<ny and j<nz):
    if y[i][0]==z[j][0]:
        curr=max(y[i][1],z[j][1])
        x.append([y[i][0],curr])        
        lastyh=y[i][1]
        lastzh=z[j][1]
        i+=1
        j+=1
    elif y[i][0]<z[j][0]:
        #print lastzh,y[i][1],y[i][0], x,j
        if lastzh==0: # left most does not matter height
            x.append([y[i][0],y[i][1]])
            #lastyh=y[i][1]
        elif y[i][1]>lastzh:
            x.append([y[i][0],y[i][1]])
            #lastyh=y[i][1]
        elif y[i][1]<lastzh and x[len(x)-1][1] != lastzh:
            #print "yo"
            x.append([y[i][0],lastzh])
        lastyh=y[i][1]        
        i+=1
        print x,lastzh,i,j
    elif y[i][0]>z[j][0]:
        #print "here",i,j,z[j][1],y[i][1]
        if lastyh==0: # left most does not matter height
            x.append([z[j][0],z[j][1]])
            #lastzh=z[j][1]
        elif lastyh<z[j][1]:
            #lastzh=z[j][1]
            x.append([z[j][0],z[j][1]])
        elif z[j][1]<lastyh and x[len(x)-1][1] != lastyh :
            #print "here",i,j,lastyh,x[len(x)-1] ,z[j][0]
            x.append([z[j][0],lastyh])
        lastzh=z[j][1]
        #print lastzh
        j+=1
    #print i,j,lastzh
    #print i,j,x
            

while(j<nz):
    x.append(z[j])
    j+=1
     
while(i<ny):
    x.append(y[i])
    i+=1
    
print x