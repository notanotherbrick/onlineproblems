# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 20:37:35 2016

@author: Hobbiton
"""
import heapq

def solution4(start, end):
      seen=set()
      q=[(0,start,[start])] #cost,current_node,path to current node
      while q:
            print q
            (path_cost,v,path)=heapq.heappop(q) # Pop out closest element
            print v            
            if v not in seen:
                seen.add(v)
                if v==end:   	# found target
                    return (path_cost,path)

                for edge_cost,u in neighbours[v]: # implemented with 32*32 board constraints
                    if u not in seen:
                        heapq.heappush(q,(edge_cost+path_cost,u,path+[u]))


neighbours={1:[[1,2]],2:[[1,3],[3,5],[1,1]],5:[[6,6],[4,4],[3,2]],3:[[1,2],[26,4]],4:[[1,6],[26,3],[1,5]],6:[[1,4],[6,5]]}

print solution4(1,6)