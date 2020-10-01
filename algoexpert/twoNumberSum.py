def twoNumberSum(array, targetSum):
    # pointers sol; best case solution
    array = sorted(array)
    leftInx = 0
    rightInx = len(array)-1
    while rightInx > leftInx:
        left = array[leftInx]
        right = array[rightInx]
        currentSum = left+right
        if currentSum == targetSum:
            return [left, right]
        elif currentSum < targetSum:
            leftInx += 1
        elif currentSum > targetSum:
            rightInx -= 1
    return []
    