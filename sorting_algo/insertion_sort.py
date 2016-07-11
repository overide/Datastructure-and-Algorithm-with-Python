#Name      : Insertion sort
#Purpose   : Of course for sorting elements! 
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------

def InsertionSort(items):
	for i in range(1,len(items)):
		j=i-1
		key = items[i]
		while (j >= 0) and items[j] > key:
			items[j+1] = items[j]
			j -= 1
		items[j+1] = key		
	return items  