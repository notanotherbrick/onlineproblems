

class graph(object):
	def __init__(self):
		from collections import defaultdict
		self.edge_list = defaultdict(set)
		#self.edge_list = set([])


	def add_edge(self,v1,v2):
		self.edge_list[v1].add(v2)
		self.edge_list[v2].add(v1)

	
	def detectCycle(self):

		def cycle(v,parent):
			visited[v] = True
			for u in self.edge_list[v]:

				if u == parent:
					continue
				elif visited[u]:
					return True
				else:
					if 	cycle(u,v):
						return True



		visited = {}

		for v in self.edge_list:
			visited[v] = False

		for v in self.edge_list:
			if visited[v] == False and cycle(v,None):
				print 'Cycle detectment'
				return False

		# No cycle
		return True



g= graph()
g.add_edge(5, 2)
g.add_edge(2, 0)
#g.add_edge(0, 5);
# #print g.graph
g.add_edge(4, 0)
#g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1);
#g.add_edge(1, 0);
g.add_edge(0, 2);
g.add_edge(3, 1);
g.add_edge(2, 3);
# g.add_edge(6, 3)


print g.detectCycle()
