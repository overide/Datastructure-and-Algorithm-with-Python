#--------------------------------------------------------------------------------------------
#Name      : Unordered Doubly Linked List
#Purpose   : Unordered Doubly Linked List implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 04/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------------
class Node:

	def __init__(self,data): # Constructor need data to initilize the node
		self.data = data
		self.next = None
		self.prev = None

	def get_data(self): # Return the data of node
		return self.data

	def get_next(self): # Return the reference of next node linked with it
		return self.next

	def get_prev(self): # Return the reference of previous node linked with it
		return self.prev

	def set_data(self,new_data): #setter for data
		self.data=new_data

	def set_next(self,new_next): #setter for next reference
		self.next=new_next

	def set_prev(self,new_prev): #setter for previous reference
		self.prev=new_prev

class DoublyList:

	def __init__(self):
		self.items = []
		self.head = None
		self.tail = None

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

	def add(self,item): # adds an item at the beginning of the list
		if self.head == None:
			t = Node(item)
			t.next=self.head
			t.prev = None
			self.head = t
			self.tail = self.head
		else:
			t = Node(item)
			t.next = self.head
			t.prev = None
			self.head.set_prev(t)
			self.head = t
		

	def size(self): # return the size of the lilnked list
		current = self.head
		nodes_count = 0
		while(current != None):
			nodes_count += 1
			current = current.get_next()
		return nodes_count

	def search(self,item): # search an item in list and return True if item is found otherwise False
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()

		return found

	def remove(self,item): # removes an item from the list 
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()

		if current.get_prev() == None and found:
			if current.get_next() != None: 
				self.head=current.get_next()
				current.get_next().set_prev(None)
			else:
				self.head = None # Only node exist in list and have to be removed
				self.tail = None
		elif current.get_prev() != None and found:
			if current.get_next() == None: # last node of list,and have to be removed
				self.tail=current.get_prev()
				current.get_prev().set_next(None)
			else:
				current.get_next().set_prev(current.get_prev())
				current.get_prev().set_next(current.get_next())
		else:
			raise Exception("No such item found in list")

	def append(self,item): # append an item to the end of the linked list
		current = self.head
		if self.head != None:
			t = Node(item)
			t.set_next = None
			t.set_prev = self.tail
			self.tail.set_next(t)
			self.tail = t
		else:
			t = Node(item)
			t.set_next = None
			t.set_prev = None
			self.head = t
			self.tail = self.head

	def insert(self,pos,item): #insert an item at specified position in the linked list
		current = self.head
		count = -1
		if pos in range(0,self.size()):
			if pos == 0:
				t = Node(item)
				t.set_next(self.head)
				t.set_prev(None)
				self.head = t
			else:
				while current != None:
					count += 1
					if count == pos-1:
						t = Node(item)
						t.set_next(current.get_next())
						t.set_prev(current)
						current.set_next(t)
					else:
						current = current.get_next()
		else:
			raise Exception("Index out of bound")

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

	def pop(self,pos = None):
	# pops an item form the end of the list if optional argument 'pos' is not provided
	# If 'pos' argument is provided then pops the item present at that position in the linked list 
		if self.head != None:
			if pos == None:
				if self.head == self.tail: # Only node exist in list and have to be removed
					v = self.head.get_data()
					self.head = None
					self.tail = None
					return v
				else:
					v=self.tail.get_data()
					self.tail=self.tail.get_prev()
					self.tail.set_next(None)
					return v
			else:
				if pos in range(0,self.size()):
					current = self.head
					count = -1
					if pos == 0: # First node to be removed
						if self.tail == self.head: # Only node exist in list and have to be removed
							v = self.head.get_data()
							self.head = None
							self.tail = None
							return v
						else:	
							v = self.head.get_data()
							self.head.get_next().set_prev(None)
							self.head = self.head.get_next()
							return v
					elif pos == self.size()-1: # Last node to be removed
						v = self.tail.get_data()
						self.tail=self.tail.get_prev()
						self.tail.set_next(None)
						return v
					else:
						while(current != None): # Other nodes in list to be removed
							count += 1
							if count == pos-1:
								v=current.get_next().get_data()
								current.set_next(current.get_next().get_next())
								current.get_next().set_prev(current)
								return v
							else:
								current=current.get_next()
				else:
					raise Exception("Index out of bound")

		else:
			raise Exception("List is empty")

	def is_empty(self): # check whether list is empty or not, return boolean value
		return self.head == None