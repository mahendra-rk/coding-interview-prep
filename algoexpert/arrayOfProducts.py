def arrayOfProducts(array):
    prods = [1 for n in array]
	
	leftProd = 1
	for i in range(len(array)):
		prods[i] = leftProd #write the product of previous nums to current index
		leftProd *= array[i] # multiple all the nums in the array, one by one

	rightProd = 1
	for i in reversed(range(len(array))):
		prods[i] *= rightProd # mutiple left and right products 
		rightProd *= array[i] # multiple all the nums in the array, one by one, right to left
	return prods

