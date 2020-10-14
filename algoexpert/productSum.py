def productSum(array, multiplier = 1):
	sum = 0
	for item in array:
		if isinstance(item, int):
			sum += item #add to sum when int
		else:
			sum += productSum(item, multiplier+1) #recursive call and increment multiplier
	return sum * multiplier
    