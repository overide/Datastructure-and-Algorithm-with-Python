 #--------------------------------------------------------------------------------------
#Name      : Binary Search Tree
#Purpose   : Binary Search Tree implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 15/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#---------------------------------------------------------------------------------------

##########################
# Class for creating BST #
##########################

class BST: 

	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,value):
		self.put(key,value)

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False

	def __delitem__(self,key):
		self.delete(key)

	def put(self,key,value): # Put a key:value pair in the BST
		if self.root:
			self._put(key,value,self.root)
			self.size += 1
		else:
			r = TreeNode(key,value)
			self.root = r
			self.size += 1

	def _put(self,key,value,current_node): #private helper method for put method
		if key < current_node.key:
			if current_node.has_left_child():
				self._put(key,value,current_node.left_child)
			else:
				current_node.left_child = TreeNode(key,value,parent=current_node)
		elif key > current_node.key:
			if current_node.has_right_child():
				self._put(key,value,current_node.right_child)
			else:
				current_node.right_child = TreeNode(key,value,parent=current_node)				
		else: #key is equal
			current_node.payload = value #replace value

	def get(self,key): # get the payload of the given key
		if self.root:
			c_node = self._get(key,self.root)
			if c_node:
				return c_node.payload
			else:
				return None
		else:
			return None

	def _get(self,key,current_node): # private helper method for get method
		if key < current_node.key:
			if current_node.has_left_child():
				return self._get(key,current_node.left_child)
			else:
				return None
		elif key > current_node.key:
			if current_node.has_right_child():
				return self._get(key,current_node.right_child)
			else:
				return None
		else: #key matched
			return current_node

	def delete(self,key): # Delete the node with given key from bst
		if self.root:
			if self.size == 1:
				if key == self.root.key:
					r = self.root.key
					self.root = None
					self.size = 0
					return r
				else:
					raise KeyError("Key not exist in Tree")
			else:
				node_to_delete = self._get(key,self.root)
				if node_to_delete:
					r = self.remove(node_to_delete)
					self.size -= 1
					return r
				else:
					raise KeyError("Key not exist in Tree")
		else:
			raise Exception ("Tree is empty")


	def remove(self,current_node): # Removes the current node from bst and maintain the bst property
		if current_node.is_leaf(): # If current node is a leaf node
			r = current_node.key
			if current_node == current_node.parent.left_child:
				current_node.parent.left_child = None
				del current_node
				return r
			else:
				current_node.parent.right_child = None
				return r
		elif current_node.has_any_children() and not current_node.has_both_children(): # if current node has only one child
			r = current_node.key
			if current_node.is_left_child():                                 # current node is left child of it's parent
				if current_node.has_left_child():
					current_node.parent.left_child = current_node.left_child
					current_node.left_child.parent = current_node.parent
					del current_node
					return r
				else:
					current_node.parent.left_child = current_node.right_child
					current_node.right_child.parent = current_node.parent
					del current_node
					return r
			else:                                                            # current node is right child of it's parent
				if current_node.has_left_child():
					current_node.parent.right_child = current_node.left_child
					current_node.left_child.parent = current_node.parent
					del current_node
					return r
				else:
					current_node.parent.right_child = current_node.right_child
					current_node.right_child.parent = current_node.parent
					del current_node
					return r
		else: 																  # current node is an interior node,have both child
			r = current_node.key
			succ = current_node.successor() 
			current_node.key = succ.key
			current_node.payload = succ.payload
			self.remove(succ)
			return r



###################################
# Class for creating nodes of BST #
###################################

class TreeNode: 

	def __init__(self,key,val,left = None,right = None,parent = None):
		self.key = key
		self.payload = val
		self.left_child = left
		self.right_child = right
		self.parent = parent
		
	def __iter__(self):
		if self:
			if self.has_left_child():
				for elem in self.left_child:
					yield elem
			yield self.key
			if self.has_right_child():
				for elem in self.right_child:
					yield elem

	def is_left_child(self): # Check if current node is the right child of it's parent 
		if self == self.parent.left_child and self.parent:
			return True
		else:
			return False

	def is_right_child(self): # Check if current node is the left child of it's parent 
		if self == self.parent.right_child and self.parent:
			return True
		else:
			return False

	def has_left_child(self): # Check if current node have left child or not
		if self.left_child:
			return True
		else:
			return False

	def has_right_child(self): # Check if current node have right child or not
		if self.right_child:
			return True
		else:
			return False

	def is_root(self): # Check if current node is root node or not
		return self.parent == None

	def is_leaf(self): # Check if current node is leaf node or not
		return not (self.left_child or self.right_child)

	def has_any_children(self): # Check if current node have any childeren or not
		if self.left_child or self.right_child:
			return True
		else:
			return False

	def has_both_children(self): # Check if current node has both children or not
		if (self.left_child and self.right_child):
			return True
		else:
			return False

	def replace_node_data(self,key,val,left,right): # Update the current node
		self.key = key 
		self.payload = val
		self.left_child = left
		self.right_child = right
		if self.has_left_child:
			self.left_child.parent = self
		if self.has_right_child:
			self.right_child.parent = self


	def successor(self): # Finds the inorder successor of the current node
		# How to find successor:
		# 1. If the node has a right child, then the successor is the smallest key in the right subtree.
		# 2. If the node has no right child and is the left child of its parent, then the parent is the successor.
		# 3. If the node is the right child of its parent, and itself has no right child, then the successor
		# to this node is the successor of its parent, excluding this node.
		succ = None
		if self.has_right_child():
			succ = self.right_child.find_min()
		else:
			if self.parent:
				if self.is_left_child():
					succ = self.parent
				else:
					self.parent.right_child = None
					succ = self.parent.successor()
					self.parent.right_child = self
		return succ

	def find_min(self): # find the node with minimum key,iterate to left node
		current = self
		while current.has_left_child():
			current = current.left_child
		return current