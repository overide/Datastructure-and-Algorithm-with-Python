#----------------------------------------------------------------------------------------------------
#Name      : Queue
#Purpose   : Queue implementation by Unordered Linked List in python for educational purpose
#Author    : Atul Kumar
#Created   : 03/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#----------------------------------------------------------------------------------------------------

from unordered_linked_list import UnorderedList

class Queue:

	def __init__(self):
		self.q = UnorderedList()

	def enque(self,items):
		self.q.add(items)

	def deque(self):
		return self.q.pop()

	def size(self):
		return self.q.size()

	def is_empty(self):
		return self.q.is_empty()

	def show(self):
		print(self.q)