def longestPeak(array):
	longest = 0
	i = 1
	while i in range(1, len(array)-1): #find the peaks
		if array[i] > array[i-1] and array[i] > array[i+1]:# find the peak
			left = i-2
			right = i+2
			while left >= 0 and array[left] < array[left+1]:#expand left 
				left -= 1
			while right < len(array) and array[right] < array[right-1]:#expand right
				right += 1
			diff = right-left-1
			longest = max(diff, longest)
			i = right #skip over the nums in the peak
		else:
			i+=1
	return longest
    