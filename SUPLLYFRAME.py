# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 15:07:30 2016

@author: Hobbiton
"""



sample='(23(43+43)940)-(32((2)1)-43)'
sample= '((11(12(3+4)'
count=0
stack=[]
res=0
curr_longest=0
streak=0

for i in xrange(len(sample)):
    if sample[i]=='(':
        count+=1
        if curr_longest>0:
            stack.append(curr_longest)
            curr_longest=0
    elif sample[i]==')':
        #print i,curr_longest
        count-=1
        if count==0:
            stack.append(curr_longest)
            res=max(res,sum(stack))
            stack=[]            
        elif count<0:
            curr_longest=0
            stack=[]
            streak=0
        else:
            streak+=curr_longest
            
            
                res=max(res,curr_longest)
                stack.append(stack.pop()+curr_longest)
            else:
                res=max()
            
            
        curr_longest=0
    
    else:
        curr_longest+=1
        


print res    

#for i in xrange(len(sample)):
#    #print i, sample[i]
#    if sample[i]=='(':
#        stack.append(i)
#    
#    elif sample[i]==')':
#        if stack:
#            #print i
#            
#            res=max(res,i-stack.pop()-1)
#        # invalid paranthese
#        else:
#            stack=[]
#            
#print res
        
            
    