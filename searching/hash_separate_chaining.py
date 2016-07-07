#------------------------------------------------------------------------------------------------------------------
#Name      : Fixed Size Hash Table
#Purpose   : Fixed Size Hash Table implementation by seprate chaining method in python for educational purpose
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#-------------------------------------------------------------------------------------------------------------------
from unordered_linked_list import UnorderedList
class HashTable:

	def __init__(self):
		self.size = 11 
		self.slot = [None] * self.size
		self.emptyCount = self.size #counts empty slot left in hash table

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,value):
		self.put(key,value)

	def __str__(self):
		htview = ""
		for x in self.slot:
			if x == None:
				htview += "None \n"
			else:
				htview += str(x)+"\n"
		return htview

	def hash_function(self,key,size):
		try:
			if key.isalnum(): #key is alpha numeric 
				sum = 0
				for ch in key:
					if ch.isdigit():
						sum+=int(ch)
					else:
						sum+=ord(ch)
				key = sum
		except:
			pass #key is integer

		return key % size

	def put(self,key,value):
		hash_value = self.hash_function(key,len(self.slot))
		if self.slot[hash_value] == None: # if slot is empty and no list is created yet!
			l = UnorderedList() # Create a list then add the key:value pair
			self.slot[hash_value] = l
			l.add(key,value)
		else:
			l = self.slot[hash_value] # if list is already present for hash value 
			if l.search(key):
				i = l.index(key)
				l.getNode(i).set_value(value) #replace
			else:
				l.add(key,value)
		
	def get(self,key):
		hash_value = self.hash_function(key,len(self.slot))
		l = self.slot[hash_value]
		i = l.index(key)
		return l.getNode(i).get_value()

	def isAnyEmpty(self):
		return self.emptyCount == 0