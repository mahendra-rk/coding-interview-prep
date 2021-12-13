# Leetcode
# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
			# check if target is in range of first and last element of each row of the matrix
            ###### Another if condition ######
            # if row[0] <= target <= row[-1]:
            ##################################
            if target in range(row[0], row[-1]+1): #  row[-1] +1 to offset the upper bound of range
                for num in row:
                    # return True if target is found 
                    if num == target:
                        return True
        return False
