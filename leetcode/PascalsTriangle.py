# Leetcode
# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for row_num in range(numRows):
            if row_num == 0:
                pascal_triangle.append([1])
            else:
                temp = [1] # first element; also resets the temp list for every iteration.
                for index in range(1, row_num):
                    # add previous row's current_index -1 and pervious row's current_index
                    temp.insert(index, pascal_triangle[row_num-1][index-1] + pascal_triangle[row_num-1][index])
                temp.append(1) # last element 
                pascal_triangle.append(temp) # append to result when all element values are calculated
        return pascal_triangle
