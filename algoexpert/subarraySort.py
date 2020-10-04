def subarraySort(array):
    minUnsorted = float("inf")
    maxUnsorted = float("-inf")
    for i in range(len(array)):
    	num = array[i]
    	if isUnsorted(i, num, array):
    		minUnsorted = min(minUnsorted, num)
    		maxUnsorted = max(maxUnsorted, num)
    if minUnsorted == float("inf") or maxUnsorted == float("-inf"):
    	return [-1, -1]
    #find position of smallest unsorted num. check for position from left of the array 
    leftIndx = 0
    while minUnsorted >= array[leftIndx]:
    	leftIndx += 1
    #find position of largest unsorted num. check for pos from right of the array
    rightIndx = len(array) -1
    while maxUnsorted <= array[rightIndx]:
    	rightIndx -= 1
    return [leftIndx, rightIndx]
    
def isUnsorted(index, num, array):
	if index == 0: # first num is greater than second num then out of order
		return num > array[index+1]
	elif index == len(array)-1: # last num is smaller than prev num then out of order
		return num < array[index-1]
	else: #check both conditions
		return num > array[index+1] or num < array[index-1]
        