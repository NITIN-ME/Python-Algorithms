class Graph:

	def __init__(self, size):
		self._size = size
		self._arr = []
		for k in range(size):
			self._arr.append([])

	def addEdge(self, u, v):
		self._arr[u].append(v)
		self._arr[v].append(u)

	def showGraph(self):
		for k in range(self._size):
			print(k," : ",end="")
			for num in self._arr[k]:
				print(num, end = "  ")
			print()


g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.showGraph()
