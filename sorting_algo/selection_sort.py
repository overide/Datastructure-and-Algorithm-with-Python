#--------------------------------------------------------------------------------------
#Name      : Selection sort
#Purpose   : Of course for sorting elements! 
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------

def SelectionSort(items):
	for i in range(len(items)-1):
		min = i
		for j in range(i+1,len(items)):
			if items[i]>items[j]:
				min = j
		if (i != min):
			items[i],items[min]=items[min],items[i]
	return items

