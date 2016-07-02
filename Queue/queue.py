#--------------------------------------------------------------------------------------
#Name      : Queue
#Purpose   : Queue implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------

class Queue:

	def __init__(self):
		self.items=[]

	def enque(self,data): # insert data at rear
		self.items.insert(0,data)

	def deque(self): # pops item form front
		try:
			p=self.items.pop()
			return p
		except Exception:
			print("Queue is Empty!")

	def size(self): # return size of the queue 
		return len(self.items)

	def show(self): # return the queue
		return self.items

	def is_empty(self):# check whether list is empty or not, return boolean values
		return self.items == []

	def front(self): # return item at front
		return self.items[len(self.items)-1]
