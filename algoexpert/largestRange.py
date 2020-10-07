def largestRange(array):
    #build hashTable for all numbers in array
    #value of keys in hashTable, visited=False 
    hashTable = {}
    for i in range(len(array)):
    	hashTable[array[i]] = False
    print(hashTable)
    longestRange = []
    longestLen = 0
    for i in range(len(array)):
    	num = array[i]
    	#For numbers not already visited
    	if not hashTable[num]:
    		hashTable[num] = True
    		left = array[i]-1
    		right = array[i]+1
    		currLen = 1
    		#find left most num in the range
    		while left in hashTable:
    			hashTable[left] = True
    			left -= 1
    			currLen += 1
    		#find right most num in the range	
    		while right in hashTable:
    			hashTable[right] = True
    			right += 1
    			currLen += 1	
    		if currLen > longestLen:
    			longestLen = currLen 
    			longestRange = [left+1, right-1] #left+1 & right-1 as nums not in array
    return longestRange
		