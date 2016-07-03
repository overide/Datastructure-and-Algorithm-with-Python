#----------------------------------------------------------------------------------------------------
#Name      : Stack
#Purpose   : Stack implementation by Unordered Linked List in python for educational purpose
#Author    : Atul Kumar
#Created   : 03/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#----------------------------------------------------------------------------------------------------

from unordered_linked_list import UnorderedList

class Stack:

	def __init__(self):
		self.s = UnorderedList()

	def push(self,items):
		self.s.add(items)

	def pop_stack(self):
		return self.s.pop(0)

	def peek_stack(self):
		return self.s.head.get_data()

	def is_empty(self):
		return self.s.is_empty()

	def size(self):
		return self.s.size()

	def show(self):
		print(self.s)