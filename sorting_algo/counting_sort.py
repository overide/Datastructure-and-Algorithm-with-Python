#------------------------------------------------------------------
#Name      : Counting Sort 
#Purpose   : Of course for sorting elements! 
#Author    : Atul Kumar
#Created   : 07/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#------------------------------------------------------------------

def counting_sort(listToSort):
	k=max(listToSort)
	tmp=[0] * (k+1)
	sortedlist=[0] * len(listToSort)
	for i in range(len(listToSort)):
		print(i)
		tmp[listToSort[i]]=tmp[listToSort[i]]+1
		# Now tmp[i] contains the number of elements equal to i 
	for i in range(1,k+1):
		tmp[i]=tmp[i]+tmp[i-1]
		#Now tmp[i] contains the number of elements less that or equal to i
	for i in reversed(range(len(listToSort))):
		sortedlist[tmp[listToSort[i]]-1]=listToSort[i]
		tmp[listToSort[i]]=tmp[listToSort[i]]-1

	return sortedlist
