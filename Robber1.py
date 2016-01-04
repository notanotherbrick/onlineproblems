# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 14:38:43 2016

@author: Gondor
"""
money=[1,2,3,1,2,3]
n=len(money)
maxLoot=[x[:] for x in [[0]*2]*(n+1)] #shallow copy

#print [n]
for i in range(n-1,-1,-1):
	maxLoot[i][1]=maxLoot[i+1][0]
	maxLoot[i][0]=max(maxLoot[i+1][0],money[i]+maxLoot[i+1][1])

print maxLoot[:n]
print max(maxLoot[0])