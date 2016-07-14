#------------------------------------------------------------------------------------
#Name      : Tree Traversal
#Purpose   : Tree Traversal methods implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 13/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#------------------------------------------------------------------------------------

def PostOrder(t): # Postorder traversal of tree
	if t != None:
		postorder(t.get_left())
		postorder(t.get_right())
		print(t.get_root())

def PreOrder(t): # Preorder traversal of tree
	if t != None:
		print(t.get_root())
		PreOrder(t.get_left())
		PreOrder(t.get_right())

def InOrder(t): # Inorder traversal of tree
	if t != None:
		InOrder(t.get_left())
		print(t.get_root())
		InOrder(t.get_right())