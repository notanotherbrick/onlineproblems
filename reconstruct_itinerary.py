# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:11:09 2016

@author: Hobbiton
"""
tickets=[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
import collections
edge = collections.defaultdict(list)
for a, b in sorted(tickets)[::-1]:
                edge[a] += b,
#for s,e in tickets:
#    edge[s].append(e)

route=[]

def visit(airport):
    while edge[airport]:
        visit(edge[airport].pop())
    route.append(airport)


visit("JKF")

print route
#print path