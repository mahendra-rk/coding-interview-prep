def zigzagTraverse(array):
    height = len(array)-1
    width = len(array[0])-1
    result = []
    row, col = 0, 0 
    isDownward = True # boolean for direction
    while not outOfBounds(row, col, height, width):
        result.append(array[row][col]) # append current position to array as we are within bounds
        if isDownward: #doing downwards
            if col == 0 or row == height: # check if first col or last row as we need to change directions
                isDownward = False #change direction
                if row == height: #  if final row
                    col += 1 # move right
                else: # in the first col and not last row 
                    row += 1 # continue downwards
            else: # not in the edges of 2D array, continue diagonally downwards
                row += 1
                col -= 1
        else: # going upward
            if row == 0 or col == width: #check if top row or last column
                isDownward = True #change direction
                if col == width: # if last column
                    row += 1 # go down
                else: # in first row and not last column
                    col += 1 # go right
            else: # not in the edges of 2D array, move diagonally upwards
                row -= 1
                col += 1
    return result


def outOfBounds(row, col, height, width):
    """ check if row & col values are within the 2D array"""
    if row < 0 or row > height: # check bounds on TOP and BOTTOM
        return True
    if col < 0 or col > width: # check bounds on LEFT and RIGHT
        return True