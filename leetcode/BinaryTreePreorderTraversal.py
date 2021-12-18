# Leetcode
# 144. Binary Tree Preorder Traversal
# TODO Iterative Solution  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorder_recursive(root, result)
        return result
    
    def preorder_recursive(self, root, result):
        if root:
            result.append(root.val)
            self.preorder_recursive(root.left, result)
            self.preorder_recursive(root.right, result)               
        