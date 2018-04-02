import math

# Pre-requisites : the input list must contain sorted distinct elements
# Below are the search algorithms.


# this is a function for linear search: if the element is found it returns the index of the element else it returns an empty list
def linearsearch(inputlist,element_to_search):
	return([index for index,list_element in enumerate(inputlist) if list_element==element_to_search])

# this is a function for binary search: if the element is found it returns the index of the element else it returns -1
def binarysearch(inputlist,element_to_search):
	low = 0
	high = len(inputlist)-1
	while high>=low:
		mid = low + (high-low)//2
		if inputlist[mid] == element_to_search:
			return(mid)
		elif inputlist[mid] > element_to_search:
			high = mid-1
		else:  
			low = mid+1
	return -1

# this is a function for jump search: if the element is found it returns the index of the element else it returns -1
def jumpsearch(inputlist,element_to_search):
	jump_size = math.floor(math.sqrt(len(inputlist)))-1
	jump_index=0
	while jump_index < len(inputlist):
		if inputlist[jump_index] == element_to_search:
			return jump_index
		elif inputlist[jump_index] < element_to_search:
			jump_index = jump_index + jump_size
		else:
			for index in range(jump_size-1,0,-1):
				jump_index -= 1
				if inputlist[jump_index] == element_to_search:
					return jump_index
				
	return -1

# this is a function for interpolation search: if the element is found it returns the index of the element else it returns -1
def interpolationsearch(inputlist,element_to_search):
	low = 0
	high = len(inputlist)-1
	mid = low + (((high - low) // (inputlist[high] - inputlist[low])) * (element_to_search - inputlist[low]))
	while mid < len(inputlist):
		if inputlist[mid] == element_to_search:
			return(mid)
		elif inputlist[mid] > element_to_search:
			high = mid-1
		elif inputlist[mid] < element_to_search:
			low = mid+1
		mid = low + (((high - low) // (inputlist[high] - inputlist[low])) * (element_to_search - inputlist[low]))
	return -1

# this is a function for exponential search: if the element is found it returns the index of the element else it returns -1
def exponentialsearch(inputlist,element_to_search):
	jump_index=1
	while jump_index < len(inputlist):
		if inputlist[jump_index] == element_to_search:
			return jump_index
		elif inputlist[jump_index] < element_to_search:
			jump_index *= 2
		else:
			min_limit = jump_index // 2
			while jump_index > min_limit:
				if inputlist[jump_index] == element_to_search:
					return jump_index
				jump_index -= 1
							
	return -1

# this is a function for fibonacci search: if the element is found it returns the index of the element else it returns -1
def fibonaccisearch(inputlist, element_to_search):
	fib1 = 1
	fib2 = 0
	fib = fib1 + fib2
	while fib < len(inputlist):
		fib2 = fib1
		fib1 = fib
		fib = fib1 + fib2
	offset = -1  # range that has been eliminated starting from the front. Initially nothing is eliminated
	index = 0
	while fib > 1:
		index = min(offset+fib2, len(inputlist)-1)
		if inputlist[index] == element_to_search:
			return index
		elif inputlist[index] > element_to_search:    # move 2 sets back
			fib = fib2
			fib1 = fib1 - fib2
			fib2 = fib - fib1
		else:     # move 1 set back
			fib = fib1
			fib1 = fib2
			fib2 = fib - fib1
			offset = index
	return -1

# this is a function for ubiquitous binarysearch: if the element is found it returns the index of the element else it returns -1
def ubiquitous_binarysearch(inputlist,element_to_search):
	low = 0
	high = len(inputlist)
	while (high-low) > 1:
		mid = low + (high-low)//2

		if inputlist[mid] > element_to_search:
			high = mid
		else:				# includes the conditions <=  
			low = mid
	if inputlist[low] == element_to_search:
		return low
	else:
		return -1
