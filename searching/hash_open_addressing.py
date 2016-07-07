#-------------------------------------------------------------------------------------------------------------------
#Name      : Fixed Size Hash Table
#Purpose   : Fixed size Hash Table implementation in python using open addressing method for educational purpose
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#-------------------------------------------------------------------------------------------------------------------

class HashTable:

	def __init__(self):
		self.size = 11 # size must be a prime number for collision resolution algo to work efficiently
		self.slot = [None] * self.size
		self.data = [None] * self.size
		self.emptyCount = self.size #counts empty slot left in hash table

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

	def rehash(self,old_hash,size): #Collision resolution with linear probing
		return (old_hash+1) % size

	def put(self,key,data):
		hash_value = self.hash_function(key,len(self.slot))
		if self.slot[hash_value] == None:
			self.slot[hash_value] =key
			self.data[hash_value] = data
			self.emptyCount -= 1
		else:
			if self.slot[hash_value] == key:
				self.data[hash_value] = data #replace
			else:
				if not self.isAnyEmpty():
					next_slot = self.rehash(hash_value,len(self.slot))
					while(self.slot[next_slot] != None and self.slot[next_slot] != key):
						next_slot = self.rehash(next_slot,len(self.slot))
					if self.slot[next_slot] == None:
						self.slot[next_slot] = key
						self.data[next_slot] = data
						self.emptyCount -= 1
					else:
						self.data[next_slot] = data #replace
				else:
					raise Exception("Hash table is full")

	def get(self,key):
		hash_value = self.hash_function(key,len(self.slot))
		data = None
		found = False
		stop = False
		pos = hash_value
		while(self.slot[pos] != None and (not found and not stop)):
			if self.slot[pos] == key:
				found = True
				data = self.data[pos]
			else:
				pos = self.rehash(pos,len(self.slot))
				if pos == hash_value:
					stop = True
		return data

	def isAnyEmpty(self):
		return self.emptyCount == 0

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)