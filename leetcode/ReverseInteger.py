#LeetCode
#7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = int(str(abs(x))[::-1])
        if reverse_num.bit_length() >= 32:
            return 0 
        if x < 0:
            reverse_num = -reverse_num
        return reverse_num