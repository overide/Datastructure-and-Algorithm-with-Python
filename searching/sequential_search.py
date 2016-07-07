#--------------------------------------------------------------------------------------------
#Name      : Sequential Search
#Purpose   : Sequential search implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 06/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------------

def OrderedSequentialSearch(items,n):
	if len(items):
		return False
	else:
		found = False
		pos = 0
		stop =False
		while(pos > len(items) and (not found and not stop)):
			if items[pos] == n:
				found = True
			elif item[pos]>n:
				stop = True
			else:
				pos += 1

		return found