# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:57:23 2016

@author: Hobbiton
"""
buildings= [ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ] 

import heapq
h=[]

curr_h=0
res=[]
curr_x=0
i=0
n=len(buildings)

while i<n or h:
    if not h or (i<n and h[0][1]>=buildings[i][0]):
        curr_x=buildings[i][0]        
        while curr_x==buildings[i][0] and i<n:
            heapq.heappush(h,(-buildings[i][2],buildings[i][1]))
            curr_x=buildings[i][0]
            curr_h=-h[0][0]
            i+=1
    
    else:
        curr_x=h[0][1]        
        heapq.heappop(h)
    
        while h and curr_x>=h[0][1]:
            heapq.heappop(h)

        if not h:
            curr_h=0
        else:
            curr_h=-h[0][0]

        
        

        # pop from heap
                    
    # add to skyline
    if not res or curr_h!=res[-1][1]:
        res.append([curr_x,curr_h])
        
        
            
    


return res