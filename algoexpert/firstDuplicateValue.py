def firstDuplicateValue(array):
    dict = {}
    for item in array:
        if dict.get(item):
            return item
        dict[item] = 1
    return -1