# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:12:27 2016

@author: Hobbiton
"""


class UndirectedGraph():
    def __init__(self):
        from collections import defaultdict
        self.graph=defaultdict(list)
        
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    
    def topsort(self):
        visited = set([])
        
        for v in self.graph:
            if v not in visited:
                if self.topsort_helper(v,v,visited) == False:
                    print 'Cycle detected'
                    return False
        
        return True
    
    def topsort_helper(self,u,last,visited):
        visited.add(u)
        for n in self.graph[u]:
            if n == last:
                continue
            elif n in visited:
                return False
            elif self.topsort_helper(n,u,visited) == False:
                return False


g= UndirectedGraph()
g.add_edge(5, 2)
g.add_edge(2, 0)
#g.add_edge(0, 5);
#print g.graph
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
#g.add_edge(3, 1);
#g.add_edge(1, 0);
#g.add_edge(0, 2);
#g.add_edge(3, 1);
#g.add_edge(2, 3);
g.add_edge(6, 3)
g.add_edge(1,6)

print g.topsort()
            
                
            
                    
        
        