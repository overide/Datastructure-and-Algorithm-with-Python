#--------------------------------------------------------------------------------------
#Name      : palindrome checker
#Purpose   : check whether given string is palindrome 
#Author    : Atul Kumar
#Created   : 29/06/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization is welcome :) 
#--------------------------------------------------------------------------------------
from deque import Deque

def Palindrome(word):
	dq=Deque()
	still_equal = True
	for ch in word:
		dq.add_rear(ch)

	while dq.size() > 1 and still_equal:
		rear = dq.remove_rear()
		front = dq.remove_front()
		if rear != front:
			still_equal = False

		return still_equal