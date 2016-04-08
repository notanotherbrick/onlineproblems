# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 14:38:43 2016

@author: Gondor
"""
money=[1]
n=len(money)
maxLoot=[x[:] for x in [[0]*3]*n] #shallow copy


#maxLoot[n-1][0]=0
#Case 1 : last place was not robbed => no constraint on 0th element
for i in range(n-2,-1,-1):
	maxLoot[i][1]=maxLoot[i+1][0]
	maxLoot[i][0]=max(maxLoot[i+1][0],money[i]+maxLoot[i+1][1])

case1= max(maxLoot[0])

maxLoot[n-1][0]=money[n-1]
for i in range(n-2,-1,-1):
	maxLoot[i][1]=maxLoot[i+1][0]
	maxLoot[i][0]=max(maxLoot[i+1][0],money[i]+maxLoot[i+1][1])

case2= maxLoot[0][1]
print max(case1,case2)
#Case 2 : last place was robbed => 0th element can only be maxLoot[0][1]