#--------------------------------------------------------------------------------------
#Name      : Deque
#Purpose   : Deque implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------

class Deque:
	def __init__(self):
		self.items=[]

	def add_rear(self,data): # add item at rear
		self.items.insert(0,data)

	def add_front(self,data): # add item at front
		self.items.append(data)

	def remove_rear(self): # remove item at rear
		try:
			p=self.items.pop(0)
			return p
		except Exception:
			print("Deque is Empty!")

	def remove_front(self): # remove item at front
		try:
			p=self.items.pop()
			return p
		except Exception:
			print("Deque is Empty!")

	def size(self): # return the size of the deque
		return len(self.items)

	def is_empty(self): # check whether deque is empty or not, return boolean value
		return self.items == []

	def show(self): # return the deque maintained 
		return self.items

	def front(self): # return the item at front 
		return self.items[len(self.items)-1]

	def rear(self): #return the item at rear
		return self.items[0]

	#def rev_str(self): 
	#	self.items.reverse()
	#	return "".join(self.items)