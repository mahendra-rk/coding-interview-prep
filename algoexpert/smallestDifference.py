def smallestDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    
    pair = []
    diff = float("inf")
    smallest = float("inf")
    indx1 = 0
    indx2 = 0
    while indx1 < len(arrayOne) and indx2 < len(arrayTwo):
        num1 = arrayOne[indx1]
        num2 = arrayTwo[indx2]
        if num1 > num2: 
            diff = num1 - num2
            indx2 += 1
        elif num2 > num1:
            diff = num2 - num1
            indx1 += 1
        else: #numbers are same, closest to 0 
            return [num1, num2]
        if diff < smallest:
            smallest = diff
            pair = [num1, num2]
            
    return pair
                