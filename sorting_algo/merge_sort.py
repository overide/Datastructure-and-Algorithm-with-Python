#------------------------------------------------------------------
#Name      : Merge sort
#Purpose   : Of course for sorting elements! 
#Author    : Atul Kumar
#Created   : 08/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#------------------------------------------------------------------

def MergeSort(a_list):
	if len(a_list)>1:
		mid = len(a_list)//2
		left_half = a_list[:mid]
		right_half = a_list[mid:]
		MergeSort(left_half)
		MergeSort(right_half)

		i = 0
		j = 0
		k = 0

		while(i < len(left_half) and j < len(right_half)):
			if left_half[i] < right_half[j]:
				a_list[k] = left_half[i]
				i += 1
			else:
				a_list[k] = right_half[j]
				j += 1
			k += 1

		while i < len(left_half):
			a_list[k] = left_half[i]
			i += 1
			k += 1

		while j < len(right_half):
			a_list[k] = right_half[j]
			k += 1
			j += 1

	return a_list