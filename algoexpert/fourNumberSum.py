def fourNumberSum(array, targetSum):
	result = []
	hashTable = {}
	for index in range(1, len(array)-1 ):
		#forward iteration
		for index2 in range(index+1, len(array)):
			currSum = array[index]+array[index2]
			print("current sum %s",currSum)
			diff = targetSum - currSum
			print("diff %s",diff)
			if diff in hashTable:
				print('match found in hashTable')
				for sumPair in hashTable[diff]:
					print(sumPair+[array[index], array[index2]])
					result.append(sumPair+[array[index], array[index2]])
					
		for index3 in range(0,index):
			print("leftNum")
			#backward iteration
			currSum = array[index]+array[index3]
			if currSum not in hashTable:
				hashTable[currSum] = [[array[index], array[index3]]]
			else:
				hashTable[currSum].append([array[index], array[index3]])	
			print("hashTable %s", hashTable)
		print("----")				
	return result