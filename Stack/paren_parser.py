#--------------------------------------------------------------------------------------
#Name      : Parantheses Balance
#Purpose   : Check whether parantheses are balanced or not using stack 
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------
from stack import Stack

def match(openp,closep):
	opens='([{'
	closes=')]}'
	return opens.index(openp)==closes.index(closep)

#This is the core function, provide sequences like '(({[]}[{()}]))'
def par_match(sequence):
	s=Stack()
	is_balanced=True
	index=0

	while len(sequence)>index and is_balanced:

		symbol=sequence[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if symbol in ")]}" and not s.is_empty():
				top=s.pop()
				if not match(top,symbol):
					is_balanced=False 
			else:
				is_balanced=False
		index+=1

	if is_balanced and s.is_empty():
		return True
	else:
		return False