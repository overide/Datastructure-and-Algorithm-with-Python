#--------------------------------------------------------------------------------------
#Name      : Bubble sort
#Purpose   : Of course for sorting elements! 
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------

def BubbleSort(items):
	for i in range(len(items)-1):
		for j in range((len(items)-1)-i):
			if items[j]>items[j+1]:
				items[j],items[j+1]=items[j+1],items[j] # Cool swapping powered by Python :D
	return items