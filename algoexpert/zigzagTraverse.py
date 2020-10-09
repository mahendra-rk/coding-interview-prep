def zigzagTraverse(array):
    #TODO add explainer comments 
    height = len(array)-1
    width = len(array[0])-1
    result = []
    row, col = 0, 0 
    isDownward = True
    while not outOfBounds(row, col, height, width):
    	result.append(array[row][col])
    	if isDownward:
    		if col == 0 or row == height:
    			isDownward = False
    			if row == height:
    				col += 1
    			else:
    				row += 1
    		else:
    			row += 1
    			col -= 1
    	else:
    		if row == 0 or col == width:
    			isDownward = True
    			if col == width:
    				row += 1
    			else:
    				col += 1
    		else:
    			row -= 1
    			col += 1
    return result
			
	
def outOfBounds(row, col, height, width):
	if row < 0 or row > height:
		return True
	if col < 0 or col > width:
		return True