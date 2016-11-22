# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


build=[[12,19,16],[2,19,2]]


x=[]

def merge(build):
    i=0
    j=0
    curr=0
    while(i<2 and j<2):
        if build[0][i]==build[1][j]:
            if i==j and i==0:
                curr=max(build[0][2],build[1][2])
                x.append([build[0][i],curr])
            elif i==j and i==1:
                x.append([build[0][i],0])
            elif i==1: # building 0 is ending 
                x.append([build[0][i],build[1][2]])
            elif j==1:
                x.append([build[0][i],build[0][2]])
            i+=1
            j+=1
   
        elif build[0][i]<build[1][j]: # if building 0 is left of building 1
            if i==0 and build[0][2]>curr:
                #h.append() # update height only if it is larger                
                x.append([build[0][i],build[0][2]])
                curr=build[0][2]
            elif i==1 and j==0: # buidling 0 ends and 1 has not started
                curr=0                
                #h.append(0) # update height only if it is larger                
                x.append([build[0][i],0])
            elif i==1 and j==1 and curr>build[1][2] : # both in continuation but building 0 is ending and building 0 is taller 
                curr=build[1][2]                
                #h.append(curr) # update height only if it is larger                
                x.append([build[0][i],curr])
            i+=1
        else:
            if j==0 and build[1][2]>curr:
                #h.append() # update height only if it is larger                
                x.append([build[1][j],build[1][2]])
                curr=build[1][2]
            elif j==1 and i==0: 
                curr=0
                #h.append(0)
                x.append([build[1][j],0])
            elif i==1 and j==1 and curr>build[0][2] : # both in continuation but building1 is ending and building 1 is taller 
                curr=build[0][2]                
                #h.append(curr) # update height only if it is larger                
                x.append([build[1][j],curr])
            j+=1
        
       # print i,j
       # print x,h,i,j
    if(j==0):
        x.append([build[1][0],build[1][2]])
        x.append([build[1][1],0])
        #h.append()
    elif j==1:
        x.append([build[1][1],0])
        
    if(i==0):
        x.append([build[0][0],build[0][2]])
        x.append([build[0][1],0])
    elif i==1:
        x.append([build[0][1],0])
    
    return x
     
print merge(build)
                    