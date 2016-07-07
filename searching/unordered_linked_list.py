#--------------------------------------------------------------------------------------
#Name      : Unordered Linked List
#Purpose   : Unordered Linked List optimized for hash tables 
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------

#Node class for creating the nodes of linked list
class Node:

	def __init__(self,key,value): # Constructor need value to initilize the node
		self.key = key
		self.value = value
		self.next = None

	def get_key(self): # Return the value of node
		return self.key

	def get_value(self): # Return the value of node
		return self.value

	def get_next(self): # Return the reference of next node linked with it
		return self.next

	def set_key(self,new_key):
		self.key = new_key

	def set_value(self,new_value): #setter for value
		self.value=new_value

	def set_next(self,new_next): #setter for next reference
		self.next=new_next

#Unordered List class 
class UnorderedList:

	def __init__(self):
		self.head = None #head keeps the reference of the first node of linked list 

	def __str__(self):
		current = self.head
		if current != None:
			lview="{"
			while(current != None):
				if current.get_next() == None:
					lview=lview + str(current.get_key()) + ":" + str(current.get_value())
				else:
					lview=lview + str(current.get_key()) + ":" + str(current.get_value()) + ","

				current = current.get_next()
			lview+="}"
			return lview
		else:
			return "List is Empty"

	def add(self,key,value): # adds an item at the beginning of the list
		t = Node(key,value)
		t.set_next(self.head)
		self.head = t

	def size(self): # return the size of the lilnked list
		current = self.head
		nodes_count = 0
		while(current != None):
			nodes_count += 1
			current = current.get_next()
		return nodes_count

	def search(self,key): # search an item in list and return True if item is found otherwise False
		current = self.head
		found = False
		while current != None and not found:
			if current.get_key() == key:
				found = True
			else:
				current = current.get_next()

		return found

	def remove(self,key): # removes an item from the list 
		current = self.head
		previous = None
		found = False
		while current != None and not found:
			if current.get_key() == key:
				found = True
			else:
				previous = current
				current = current.get_next()
		if previous == None and found:
			self.head=current.get_next()
		elif previous != None and found:
			previous.set_next(current.get_next())
		else:
			raise Exception("No such item found in list")
	

	def append(self,key,value): # append an item to the end of the linked list
		current = self.head
		if self.head != None:
			while current.get_next() != None:
				current = current.get_next()
			t=Node(key,value)
			t.set_next(current.get_next())
			current.set_next(t) 
		else:
			t=Node(key,value)
			t.set_next(None)
			self.head = t

	def insert(self,pos,key,value): #insert an item at specified position in the linked list
		current = self.head
		count = -1
		if pos in range(0,self.size()):
			if pos == 0:
				tmp = Node(key,value)
				tmp.set_next(current)
				self.head=tmp
			else:
				while current != None :
					count+=1
					if count == pos-1:
						tmp = Node(key,value)
						tmp.set_next(current.get_next())
						current.set_next(tmp)
					else:
						current = current.get_next()
		else:
			raise Exception("Index out of bound")

	def index(self,key): # return the index of the first item searched in case of duplicate items
		current = self.head
		found = False
		count = 0
		atPos = None
		while current != None and not found:
			count += 1
			if current.get_key() == key:
				found = True
				atPos = count-1
			else:
				current = current.get_next()

		if found:
			return atPos
		else:
			raise Exception("No such item in List found")

	def getNode(self,index): # Return node at given index
		current = self.head
		pos = -1
		found = False
		node = None
		if index in range(self.size()):
			while(current != None and not found):
				pos += 1
				if pos == index:
					found = True
					node = current
				else:
					current = current.get_next()
			if found:
				return node
			else:
				raise Exception("No such item in list found")
		else:
			raise Exception("Index out of range")


	def pop(self,pos=None):
	# pops an item form the end of the list if optional argument 'pos' is not provided
	# If 'pos' argument is provided then pops the item present at that position in the linked list 
		current = self.head
		if self.head != None:
			if pos == None:
				if self.size() == 1:
					v=self.head.get_key()
					self.head = None
					return v
				else:
					while(current.get_next().get_next() != None):
						current = current.get_next()
					v = current.get_next().get_key()
					current.set_next(None)
					return v
			else:
				current = self.head
				count = -1
				if pos in range(0,self.size()):
					if pos == 0:
						v=self.head.get_key()
						self.head=self.head.get_next()
						return v
					else:
						while current != None:
							count+=1
							if count == pos-1:
								v = current.get_next().get_key()
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