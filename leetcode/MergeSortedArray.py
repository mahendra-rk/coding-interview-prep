# Leetcode
# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # check if 2nd array has any value
        if nums2:
            #pointers for the 2 arrays 
            index1 = index2 = 0 
            while index1 < m and index2 < n:
                # if the currect element of nums1 is bigger than the current element of nums2, 
                # insert num2 element to nums1 at current position.
                if nums1[index1] > nums2[index2]:
                    nums1.insert(index1, nums2[index2])
                    index2 += 1 # increment nums2 pointer
                    m += 1 #increment m as the insert operation has pushed elements to the right
                #always increment nums1 pointer; 
                # the current value of nums1 is in the correct position or 
                # it was moved one position right in the array to accomodate element from nums2
                index1 += 1 
            # Handle extra 0s in nums1
            if index2 < n:
                # replace all the zeros at the end of nums1 with the rest of the values of nums2 
                # that are not in nums1
                nums1[m:] = nums2[index2:]
            else:
                # otherwise, we inserted all `n` elements of nums2 into nums1 and,
                # in this case, we need to delete the last `n` elements of nums1 
                # (they are the zeros that we pushed back to acomodate the nums2 values)
                del nums1[-n:]                
