#----------------------------------------------------------------------------------------------------
#Name      : Heap sort
#Purpose   : Heap Sort implementation using Maximum Binary Heap in python for educational purpose
#Author    : Atul Kumar
#Created   : 11/07/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#Any corrections and suggestions for optimization are welcome :) 
#----------------------------------------------------------------------------------------------------
from max_binary_heap import MaxBinHeap

def HeapSort(a_list): # Runs in O(n lg n)
	bh = MaxBinHeap()
	bh.build_heap(a_list)
	i = bh.current_size
	while (i > 1):
		bh.heap[1],bh.heap[i] = bh.heap[i], bh.heap[1]
		bh.current_size -= 1
		bh.perc_down(1)
		i -= 1
	return bh.heap[1:]