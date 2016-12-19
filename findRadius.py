# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:44:02 2016

@author: Hobbiton
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort() 
        #print houses
        #print heaters

        if not houses or not heaters:
            return 
        rad = abs(heaters[0]- houses[0])
        home = 1
        heat = 0
        while home < len(houses):
            print rad
            if heat == len(heaters) - 1:
                # reached last heater
                rad = max(rad,abs(heaters[-1]-houses[-1]))
                break
            else:
                curr = abs(houses[home] - heaters[heat])
                nex = abs(houses[home] - heaters[heat+1])
                if curr > nex:
                    rad = max(rad,nex)
                    heat+=1
                else:
                    rad = max(rad,curr)
            
            home+=1
        
        return rad

S = Solution()
print S.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])
                
                
        
        
        