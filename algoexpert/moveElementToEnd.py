def moveElementToEnd(array, toMove):
    result = []
    for num in array:
        if num == toMove:
            result.insert(len(result), num)
        else:
            result.insert(0, num)
    return result