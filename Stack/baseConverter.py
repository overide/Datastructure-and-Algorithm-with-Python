#--------------------------------------------------------------------------------------
#Name      : Any Base Converter
#Purpose   : Convert base 10 to any base
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------
from stack import Stack

def convert(number,toBase):
	digits='0123456789ABCDEF'
	s=Stack()
	while number>0:
		rem=number%toBase
		s.push(rem)
		number=number//toBase

	op_str=""
	while not s.is_empty():
		op_str=op_str+digits[s.pop()]

	return op_str