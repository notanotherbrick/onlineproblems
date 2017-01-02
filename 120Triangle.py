


class heapq(object):
	def __init__(self):
		self.array = []

	def heappush(self, element):
		self.array.append(element)
		self.heapify_up(len(self.array)-1)

	def heapprint(self):
		print self.array

	def heappop(self):
		if not self.array:
			return
		if len(self.array) == 1:
			return self.array.pop()

		self.array[0], self.array[-1]  = self.array[-1], self.array[0]
		res = self.array.pop()
		i = 0 

		while i < len(self.array)/2:
			if self.array[2*i][0] <  self.array[2*i + 1][0] and self.array[2*i][0] < self.array[i][0] :
				self.array[2*i][0], self.array[i][0] = self.array[i][0], self.array[2*i][0]
				i = 2*i
			elif self.array[2*i + 1][0] <  self.array[2*i][0] and self.array[2*i + 1][0] < self.array[i][0] :
				self.array[2*i + 1][0], self.array[i][0] = self.array[i][0], self.array[2*i + 1][0]
				i = 2*i + 1	
			else:
				break


		#print 'at end', self.array
		return res



	def heapify_up(self, i):
		while i>0 and self.array[i/2] > self.array[i]:
			self.array[i/2], self.array[i] = self.array[i], self.array[i/2]
			i = i/2 

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#triangle = [[-1],[-2,-3]]

for i in xrange(1,len(triangle)):
	for j in xrange(len(triangle[i])):
		if j ==0:
			triangle[i][j] += triangle[i-1][0]
		elif j == len(triangle[i]):
			triangle[i][j] += triangle[i-1][j-1] 
		else:
			triangle[i][j] += min (triangle[i-1][j],triangle[i-1][j-1])

return min(triangle[-1])

