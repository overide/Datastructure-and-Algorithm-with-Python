#--------------------------------------------------------------------------------------
#Name      : Stack
#Purpose   : Stack implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 28/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------


class Stack:

	def __init__(self):
		self.items=[]

	def push(self,data): # push an item in stack
		self.items.append(data)

	def pop(self): # pop an item from stack
		try:
			p=self.items.pop()
			return p
		except Exception:
			print("Stack is Empty!")

	def peek(self): # return the item at top of stack
		return self.items[len(self.items)-1]

	def is_empty(self): # 
		return self.items == []

	def size(self): # check whether stack is empty or not, return boolean value
		return len(self.items)

	def show(self): # return the stack maintained
		return self.items

	def rev_str(self): # reverse the stack
		return self.items.reverse()
