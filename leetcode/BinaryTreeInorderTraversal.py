# Leetcode
# 94. Binary Tree Inorder Traversal
# TODO Iterative Solution   

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder_recursive(root, result)
        return result
    
    def inorder_recursive(self, root, result):
        if root:
            self.inorder_recursive(root.left, result)
            result.append(root.val)
            self.inorder_recursive(root.right, result)            
