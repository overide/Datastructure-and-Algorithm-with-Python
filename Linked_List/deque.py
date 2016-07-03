#----------------------------------------------------------------------------------------------------
#Name      : Deque
#Purpose   : Deque implementation by Unordered Linked List in python for educational purpose
#Author    : Atul Kumar
#Created   : 03/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#----------------------------------------------------------------------------------------------------

from unordered_linked_list import UnorderedList

class Deque:

	def __init__(self):
		self.dq = UnorderedList()

	def add_rear(self,item):
		self.dq.add(item)

	def add_front(self,item):
		self.dq.append(item)

	def remove_rear(self):
		return self.dq.pop(0)

	def remove_front(self):
		return self.dq.pop()

	def size(self):
		return self.dq.size()

	def is_empty(self):
		return self.dq.is_empty()

	def show(self):
		print(self.dq)