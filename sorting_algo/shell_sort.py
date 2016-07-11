#--------------------------------------------------------------------------------------
#Name      : Shell sort
#Purpose   : Of course for sorting elements! 
#Author    : Atul Kumar
#Created   : 08/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

# In this implemenmtation the increments is as n/2,n/4,n/8...and so on !
#Any corrections and suggestions for optimization are welcome :) 
#--------------------------------------------------------------------------------------


def ShellSort(items):
	sublist_count = len(items)//2 
	while(sublist_count > 0):
		for start_position in range(sublist_count):
			gap_inseriton_sort(items,start_position,sublist_count)
		#   print("After increment of count "+str(sublist_count)+" the list is: "+str(items))
		sublist_count = sublist_count//2
	return items
	
def gap_inseriton_sort(items,start,gap):
	for i in range((start+gap),len(items),gap):
		j=i-gap
		key = items[i]
		while (j >= 0) and items[j] > key:
			items[j+gap] = items[j]
			j -= gap
		items[j+gap] = key		
