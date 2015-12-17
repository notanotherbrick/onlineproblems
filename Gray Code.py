# class Solution(object):
#     def grayCode(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         node=self.makeGraph(n)
#         self.printGraph()
        
#     def makeGraph(n):
        
        
# class node:
#     int key
#     node top,bottom
#     node parent
        

# if name=__main__
# Solution()

n=5
L=[0,1]
#M=[]
for i in range(2, n+1):
	#print "I is ",i
	L=L+L[::-1]
	#print L

	for ele in range(0,pow(2,i-1)):
		L[ele]=int("0"+str(L[ele]))
	for ele in range(pow(2,i-1),pow(2,i)):
		L[ele]=int("1"+str(L[ele]))

	#print "after", L



print "final output", len(L), "\n",L

# i=0
# for x in L:
#     for i in xrange(len(x)):
#         tem



def grayCode(n):
    """
    :type n: int
    :rtype: List[int]

    """
    if n<1:
        return [0]
    if (n==1):
        return [0,1]
    res = grayCode( n-1)
    x=pow(2,n-1)
    for i in range(x-1,-1,-1):
        res.append(res[i]+x)
    return res


print grayCode(5)