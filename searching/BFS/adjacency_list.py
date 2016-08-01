#--------------------------------------------------------------------------------------------
#Name      : Adjacency List
#Purpose   : Adjacency list implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 29/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------------

from unordered_linked_list_vertex import UnorderedList as VertexList
from unordered_linked_list_edge import  UnorderedList as EdgeList

class AdjacencyList :

	def __init__(self):
		self.vertex_list = VertexList()

	def __str__(self):
		return self.vertex_list.__str__()

	def insert_vertex(self,key): #insert a vertex in adjacency list
		self.vertex_list.append(key)

	def insert_edge(self,origin,dest): # Insert an edge (source,destination) pair 
		origin_node = self.vertex_list.getNode(self.vertex_list.index(origin))
		if origin_node.edge != None :
			origin_node.edge.append(self.vertex_list.getNode(self.vertex_list.index(dest))) # appending destination vertex node reference
		else:
			origin_node.edge = EdgeList()
			origin_node.edge.append(self.vertex_list.getNode(self.vertex_list.index(dest))) # appending destination vertex node reference
