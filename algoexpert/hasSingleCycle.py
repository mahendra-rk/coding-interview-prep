def hasSingleCycle(array):
	jumpCounter = 0
	current = 0
	while jumpCounter < len(array): #as single cycle will have only len(array) number of jumps
		if current == 0 and jumpCounter != 0 : # if not visited all elements but we are back at starting point
			return False
		current = nextIndex(current, array)
		jumpCounter += 1
	return current == 0	# will be true if all elements are visited and we are back at starting point 
	

def nextIndex(index, array):
	jump = array[index]
	potentialIndex = (index + jump) % len(array) # formula for getting next index
	if potentialIndex < 0: #if negative num
		return potentialIndex + len(array)
	return potentialIndex
		