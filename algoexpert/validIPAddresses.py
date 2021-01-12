def validIPAddresses(string):
    results = []
	for i in range(1, min(len(string), 4)):
		currentAddress = ['', '', '', '']
		currentAddress[0] = string[:i]
		if not isValid(currentAddress[0]):
			continue
		for j in range(i+1, min(len(string), i+4)):
			currentAddress[1] = string[i:j]
			if not isValid(currentAddress[1]):
				continue
			for k in range(j+1, min(len(string), j+4)):
				currentAddress[2] = string[j:k]
				currentAddress[3] = string[k:]		
				if isValid(currentAddress[2]) and isValid(currentAddress[3]):
					results.append(".".join(currentAddress))
	return results

def isValid(part):
	intPart = int(part)
	if intPart>255:
		return False
	return len(part) == len(str(intPart)) # checking for leading 0s
		
	
