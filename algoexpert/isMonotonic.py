def isMonotonic(array):
    nonIncreasing = True
    nonDecreasing = True
    index = 0
    while index < len(array)-1:
        if array[index] > array[index+1]:
            nonIncreasing = False
        if array[index] < array[index+1]:
            nonDecreasing = False
        index +=1
    return nonIncreasing or nonDecreasing
