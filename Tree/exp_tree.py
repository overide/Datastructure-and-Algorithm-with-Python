#----------------------------------------------------------------------------
#Name      : Expression Tree
#Purpose   : Expression Tree implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 12/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#----------------------------------------------------------------------------

from binary_tree import BinaryTree
from stack import Stack
import operator

def PostOrder(t): #post order Traversal of a tree
	if(t != None):
		PostOrder(t.get_left())
		PostOrder(t.get_right())
		print(t.get_root(), end = ",")

def evaluate(t): # Evaluate a expression tree
	oper = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	left = t.get_left()
	right = t.get_right()
	if left and right:
		return oper[t.get_root()](evaluate(left),evaluate(right))
	else:
		return t.get_root()


def BuildExpTree(exp): #build the expression tree
	exp_tokens = exp.split()
	prnt_stack = Stack()
	exp_tree = BinaryTree('')
	prnt_stack.push(exp_tree) # parent of root node is itself, so pushing it in stack!
	operators = ['+','-','*','/']
	current_tree = exp_tree

	for token in exp_tokens: 
		if token == '(':
			current_tree.insert_left('')
			prnt_stack.push(current_tree)
			current_tree = current_tree.get_left()


		elif token not in (str(operators) + ")"):
			current_tree.set_root(int(token))
			current_tree = prnt_stack.pop()

		elif token in operators:
			current_tree.set_root(token)
			current_tree.insert_right('')
			prnt_stack.push(current_tree)
			current_tree = current_tree.get_right()

		elif token == ')':
			current_tree = prnt_stack.pop()

		else:
			raise ValueError

	return exp_tree