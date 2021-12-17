# Leetcode
# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        elements = {'(': ')', '{': '}', '[': ']'}
        
        for i in s:
            if i in elements:
                stack.append(i)
            elif stack and i == elements[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
