#--------------------------------------------------------------------------------------
#Name      : Ordered Linked List
#Purpose   : Ordered Linked List implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 03/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------

#Node class for creating the nodes of linked list
class Node:

	def __init__(self,data): # Constructor need data to initilize the node
		self.data = data
		self.next = None

	def get_data(self): # Return the data of node
		return self.data

	def get_next(self): # Return the reference of next node linked with it
		return self.next

	def set_data(self,new_data): #setter for data
		self.data=new_data

	def set_next(self,new_next): #setter for next reference
		self.next=new_next

# Ordered Linked List class 
class OrderedList:

	def __init__(self):
		self.head = None #head keeps the reference of the first node of linked list 

	def __str__(self):
		current = self.head
		if current != None:
			lview="[ "
			while(current != None):
				lview=lview + str(current.get_data())+" "
				current = current.get_next()
			lview+="]"
			return lview
		else:
			return "List is Empty"

	def add(self,data): #adds an item in accending order
		current = self.head
		previous = None
		stop = False
		while(current != None ) and (not stop):
			if current.get_data() >= data:
				stop = True
			else:
				previous = current
				current = current.get_next()	
		t = Node(data) 			
		if previous == None:
			t.set_next(self.head)
			self.head = t
		else:
			t.set_next(current)
			previous.set_next(t)

	def size(self): #return the size of the linked list
		current = self.head
		nodes_count = 0
		while(current != None):
			nodes_count += 1
			current = current.get_next()
		return nodes_count

	def search(self,item): # search an item in list and return True if item is found otherwise False
		current = self.head
		found = False
		stop = False 
		while current != None and (not found and not stop):
			if current.get_data() == item:
				found = True
			elif current.get_data() > item:
				stop = True
			else:
				current = current.get_next()

		return found

	def remove(self,item): # removes an item from the list 
		current = self.head
		previous = None
		found = False
		stop = False
		while current != None and (not found and not stop):
			if current.get_data() == item:
				found = True
			elif current.get_data() > item:
				stop = True
			else:
				previous = current
				current = current.get_next()
		if previous == None and found: # removing item at position 0
			self.head=current.get_next()
		elif previous != None and found:
			previous.set_next(current.get_next())
		else:
			raise Exception("No such item found in list")
	

	def index(self,item): # return the index of the first item searched in case of duplicate items
		current = self.head
		found = False
		count = 0
		atPos = None
		while current != None and not found:
			count += 1
			if current.get_data() == item:
				found = True
				atPos = count-1
			else:
				current = current.get_next()

		if found:
			return atPos
		else:
			raise Exception("No such item in List found")


	def pop(self,pos=None):
	# pops an item form the end of the list if optional argument 'pos' is not provided
	# If 'pos' argument is provided then pops the item present at that position in the linked list 
		current = self.head
		if self.head != None:
			if pos == None:
				if self.size() == 1:
					v=self.head.get_data()
					self.head = None
					return v
				else:
					while(current.get_next().get_next() != None):
						current = current.get_next()
					v = current.get_next().get_data()
					current.set_next(None)
					return v
			else:
				current = self.head
				count = -1
				if pos in range(0,self.size()):
					if pos == 0:
						v=self.head.get_data()
						self.head=self.head.get_next()
					else:
						while current != None:
							count+=1
							if count == pos-1:
								v = current.get_next().get_data()
								current.set_next(current.get_next().get_next())
							else:
								current = current.get_next()

						return v
				else:
					raise Exception("Index out of bound")
		else:
			raise Exception("List is empty")

	def is_empty(self): # check whether list is empty or not, return boolean value
		return self.head == None