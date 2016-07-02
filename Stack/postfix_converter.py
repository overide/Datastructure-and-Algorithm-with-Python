#--------------------------------------------------------------------------------------
#Name      : Infix 2 postfix
#Purpose   : Infix to postfix convertor 
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------

from stack import Stack

def toPostfix(exp): #Example Expression 'A + (B * C) + D', don't forget spaces !!!
	op_prec={'*':3,'/':3,'+':2,'-':3,'(':1}
	s=Stack()
	tokens=exp.split()
	op_list=[]
	op_parn=['+','-','/','*','(',')']

	for symbol in tokens:
		if symbol not in op_parn:
			op_list.append(symbol)

		elif symbol == '(':
			s.push(symbol)

		elif symbol == ')':
			top_token=s.pop()
			while top_token != '(':
				op_list.append(top_token)
				top_token=s.pop()

		else:
				while((not s.is_empty()) and op_prec[symbol]<=op_prec[s.peek()]):
					op_list.append(s.pop())
				s.push(symbol)

	while(not s.is_empty()):
		op_list.append(s.pop())

	return "".join(op_list)