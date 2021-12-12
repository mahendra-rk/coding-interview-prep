# Leetcode
# 566. Reshape the Matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_shape = len(mat) * len(mat[0])
        new_shape = r * c 
        
        if old_shape != new_shape: # if new shape is not equal to new shape return matrix. 
            return mat
        
        flat_array = []
        for row in mat:
            for num in row:
                flat_array.append(num)
        
        new_mat = []
        index = 0 # To keep track of elements from the flat_array
        for i in range(r): 
            row = []
            for j in range(c):
                row.append(flat_array[index])
                index += 1 # increment index after every append
            new_mat.append(row)
            row = [] # reset row after append to new matrix 
        return new_mat
