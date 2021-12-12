def threeNumberSum(array, targetSum):
    array = sorted(array)
    result = []
    for i in range(len(array)-2):
        first = i
        left = i+1
        right= len(array)-1
        while left < right:
            currSum = array[first]+array[left]+array[right]
            if currSum == targetSum:
                result.append([array[first],array[left],array[right]])
                left+=1
                right-=1
            elif currSum < targetSum:
                left += 1
            elif currSum > targetSum:
                right -=1
    return result