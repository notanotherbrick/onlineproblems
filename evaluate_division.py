# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:18:46 2016

@author: Hobbiton
"""
equations=[ ["a","b"],["b","c"] ]
values=[2.0,3.0]
[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]

from collections import defaultdict
graph=defaultdict(dict)
for i in xrange(len(values)):
    u,v=equations[i]
    graph[u][u]=graph[v][v]=1.0
    graph[u][v]=values[i]
    graph[v][u]=1/values[i]


print graph
dist=[[float('inf')]*len(graph) for _ in xrange(len(graph))]