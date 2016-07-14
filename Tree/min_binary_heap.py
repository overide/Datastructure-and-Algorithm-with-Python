#------------------------------------------------------------------------------
#Name      : Minimum Binary Heap
#Purpose   : Minimum Binary Heap implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 11/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#------------------------------------------------------------------------------

class MinBinHeap:

	def __init__(self): # Well yeah! constructor!
		self.heap = [0]
		self.current_size = 0

	def insert(self,k): # Insert an element in heap
		self.heap.append(k)
		self.current_size += 1
		self.perc_up(self.current_size)

	def del_min(self): # Delete minimum element in heap 
		if self.current_size >= 1: 
			min_val = self.heap[1]
			self.heap[1] = self.heap[self.current_size]
			self.current_size -= 1
			self.heap.pop()
			self.perc_down(1)
			return min_val
		else:
			raise Exception ("List is empty")

	def parent(self,pos): # return the index of the parent
		return pos // 2

	def left(self,pos): # return the index of left child
		return pos*2

	def right(self,pos): # return the index of right child
		return (pos*2)+1

	def perc_up(self,i): # perc for "percolation", maintain the minimum heap property when a new element is added in heap
		while(self.parent(i)>0) :
			if self.heap[self.parent(i)] > self.heap[i]:
				self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
			i = self.parent(i)

	def perc_down(self,i): # perc for "percolation", maintain the minimum heap property when minimum element is deleted from heap ,takes O(lg n)
		while( i*2 <= self.current_size):
			l_child = self.left(i)
			r_child = self.right(i)
			min_val = None
			if l_child <= self.current_size:
				if self.heap[l_child]<self.heap[i]:
					min_val = l_child
				else:
					min_val = i

				if r_child <= self.current_size:
					if self.heap[r_child] < self.heap[min_val]:
						min_val = r_child

				if min_val != i:
					self.heap[i],self.heap[min_val] = self.heap[min_val],self.heap[i]
					i = min_val
				else:
					break

	def build_heap(self,a_list): #build heap from the given list, runs in O(n).Refer book for crazy mathematics envolved in this!
		self.current_size = len(a_list)
		self.heap.extend(a_list)
		i = self.current_size // 2
		while (i > 0):	
			self.perc_down(i)
			i -= 1


	def get_min(self): # Return the minimum element in the heap
		return self.heap[1]