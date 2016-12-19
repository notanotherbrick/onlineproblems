# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:45:00 2016

@author: Hobbiton
"""

'''
This only works for Directed Graphs
'''

from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph=defaultdict(list)
        self.vertex=set([])
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.vertex.add(u)
        self.vertex.add(v)
    
    def topsort(self):
        visited={}
        for v in self.vertex:
            visited[v]='w'
        
        order=[]
        for v in self.graph:
            if self.topsort_helper(v,visited,order) == -1:
                print 'cycle detected'
                return
        print order[::-1]
    
    def topsort_helper(self,v,visited,order):
        print v, visited
        if visited[v]=='g': # in process
            return -1
        elif visited[v]=='w': # not explored
            visited[v]='g'
            if v in self.graph:
                for u in self.graph[v]:
                    if self.topsort_helper(u,visited,order)==-1:
                        return -1
                
            
            visited[v]='b' # closed
            order.append(v)

g= Graph()
g.add_edge(5, 2);
g.add_edge(2, 0);
g.add_edge(0, 5);
print g.graph
#g.add_edge(4, 0);
#g.add_edge(4, 1);
#g.add_edge(2, 3);
#g.add_edge(3, 1);
#g.add_edge(1,0);
#g.add_edge(0,2);
#g.add_edge(3, 1);
#g.add_edge(2, 3);
#g.add_edge(1, 3);

g.topsort()
 
            
        