#--------------------------------------------------------------------------------------------
#Name      : Binary Search
#Purpose   : Binary search implementation in python for educational purpose
#Author    : Atul Kumar
#Created   : 06/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------------

def BinarySearch(items,n):
	if len(items) == 0:
		return False
	else:
		first = 0
		last = len(items)-1
		found =False
		while(first <= last and not found):
			mid= (first+last)//2
			if n == items[mid]:
				found = True
			elif n>items[mid]:
				first = mid+1
			else:
				last = mid-1
			
		return found
