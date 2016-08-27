#--------------------------------------------------------------------------------------
#Name      : Depth First Search
#Purpose   : Depth First Search implementation in python, as per CLRS
#Author    : Atul Kumar
#Created   : 27/08/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------

import pprint

class Node:

	def __init__(self,k):
		self.key = k
		self.p = None	# predecessor
		self.color = 'W'
		self.d = 0		# distance from source
		self.d_time = 0 # Discovery time
		self.f_time = 0 # Final time

	def get_key(self):
		return self.key

	def get_predecessor(self):
		return self.p

	def get_color(self):
		return self.color

	def get_distance(self):
		return self.d

	def get_dtime(self):
		return self.d_time

	def get_ftime(self):
		return self.f_time

	def set_key(self,k):
		self.key = k

	def set_predecessor(self,p):
		self.p = p

	def set_color(self,c):
		self.color = c

	def set_distance(self,d):
		self.d = d

	def set_dtime(self,t):
		self.d_time = t

	def set_ftime(self,t):
		self.f_time = t

class AdjList:

	def __init__(self):
		self.adjlist = []

	def __iter__(self):
		for i in self.adjlist:
			yield i

	def append(self,n):
		self.adjlist.append(n)

class Graph:

	def __init__(self,v):
		self.arry = [None]*v
		self.vertex={}
		self.time = 0

	def add_vertex(self,n):
		tmp = Node(n)
		self.vertex[n]=tmp

	def add_edge(self,u,v):

		if self.arry[u] == None :
			self.arry[u] = AdjList()

		self.arry[u].append(self.vertex[v])

	def _DFS_visit(self,u):
		self.time+=1
		print(u.get_key(),end=" ")
		u.set_color('G')
		u.set_dtime(self.time) 

		for v in self.arry[u.get_key()]:
			if v.get_color() == 'W':
				v.set_color('G')
				v.set_predecessor(u)
				v.set_distance(u.get_distance()+1)
				self._DFS_visit(v)

		self.time+=1
		u.set_ftime(self.time)
		u.set_color('B')

	def DFS(self):
		print("Running DFS...")
		for u in self.vertex.values():
			if u.get_color() == 'W':
				self._DFS_visit(u)
		print("\n")
		self.time = 0

def main():
	g = Graph(6)
	g.add_vertex(0)
	g.add_vertex(1)
	g.add_vertex(2)
	g.add_vertex(3)
	g.add_vertex(4)
	g.add_vertex(5)

	g.add_edge(0,1)
	g.add_edge(0,3)
	g.add_edge(1,2)
	g.add_edge(2,3)
	g.add_edge(3,1)
	g.add_edge(4,2)
	g.add_edge(4,5)
	g.add_edge(5,5)
	
	g.DFS()

if __name__ == "__main__":
	main()