#----------------------------------------------------------------------------
#Name      : Simple Binary Tree
#Purpose   : Simple Binary Tree implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 09/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#----------------------------------------------------------------------------

class BinaryTree:
	def __init__(self,root):
		self.key = root
		self.left_child = None
		self.right_child = None

	def insert_left(self,new_node):
		if self.left_child != None:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t
		else:
			self.left_child = BinaryTree(new_node)

	def insert_right(self,new_node):
		if self.right_child != None:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t
		else:
			self.right_child = BinaryTree(new_node)

	def get_right(self):
		return self.right_child

	def get_left(self):
		return self.left_child

	def set_root(self,obj):
		self.key = obj

	def get_root(self):
		return self.key
