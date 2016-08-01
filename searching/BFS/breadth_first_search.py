#--------------------------------------------------------------------------------------------
#Name      : Breadth First Search
#Purpose   : Breadth First Search implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 29/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------------

from adjacency_list import AdjacencyList
from queue import Queue

# You have to provide a object of adjacency_list and a source vertex eg. BFS(adj,'s')
def BFS(graph,source): 
	q = Queue()
	source = graph.vertex_list.getNode(graph.vertex_list.index(source))
	for u in graph.vertex_list:
		if u != source:
			u.set_color('W')

	source.set_color('G')
	source.set_distance(0)

	q.put(source)
	while not q.empty():
		u = q.get()
		print(" vertex : "+str(u.get_key())+", Distance from source : "+str(u.get_distance()))
		try:
			for v in u.edge:
				v = v.get_key()
				if v.get_color() == 'W':
					v.set_color('G')
					v.set_parent(u)
					v.set_distance(u.get_distance() + 1)
					q.put(v)
			u.set_color = 'B'
		except Exception as exp:
			pass