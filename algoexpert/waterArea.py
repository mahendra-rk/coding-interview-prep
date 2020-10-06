def waterArea(heights):
	leftMax = 0
	rightMax = 0
	result = [0] * len(heights)
	for i in range(len(heights)):
		#find and store max height on the left for a given position
		if heights[i] > leftMax:
			leftMax = heights[i]
		result[i] = leftMax
	print(result)
	for i in reversed(range(len(heights))):
		# find max height on the right for a given position
		height = heights[i]
		if height > rightMax:
			rightMax = height
		# Since we have left and right height, we can find the area which can hold water			
		minHeight = min(result[i], rightMax)
		if height < minHeight:
			result[i] = minHeight - height
		else:
			result[i] = 0
	print(result)		
	return sum(result)
	