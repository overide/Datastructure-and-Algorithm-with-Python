#--------------------------------------------------------------------------------------
#Name      : Postfix Evaluator
#Purpose   : Evaluate postfix expression 
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------

from stack import Stack

def evalPostfix(exp): #Example Expression '7 8 + 3 2 + /', don't forget those spaces!!!
	s=Stack()
	token_stream=exp.split()

	try:
		for token in token_stream:
			if token in '0123456789':
				s.push(token)
			else:
				op1=s.pop()
				op2=s.pop()
				a=evaluate(token,op1,op2)
				s.push(a)
		return s.pop()
	except:
		print("Please Check you Postfix Expression!")

def evaluate(operator,operand1,operand2):
	if operator == '+':
		return int(operand2) + int(operand1)
	if operator == '-':
		return int(operand2) - int(operand1)
	if operator == '*':
		return int(operand2) * int(operand1)
	if operator == '/':
		return int(operand2) / int(operand1)
