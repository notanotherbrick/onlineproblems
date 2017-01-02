class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == s[::-1]:
            return s
            
        t = s + '#' + s[::-1]
        
        kmp = [0] * len(t)
        
        i = 1

        curr = 0 

        while i < len(t):
        	# continue string match
        	
        	if t[curr] == t[i]:
    				curr += 1 
    				kmp[i] = curr
    				i += 1

    		# nothing worked
    		else:
    			if curr != kmp[curr]:
	    			
	    			curr = kmp[curr - 1]


	    		else:
	    			kmp[i] = 0
	    			i+=1
	    			curr = 0 
	    	#print t[i],i, curr, kmp[curr] , t[curr]


        print kmp, t
        end_idx = kmp[-1]
        
        if end_idx:
           #print end_idx
           return s[end_idx:][::-1] + s
        else:
            return s[1:][::-1] + s

            
S = Solution()
print S.shortestPalindrome("aacecaaa")
