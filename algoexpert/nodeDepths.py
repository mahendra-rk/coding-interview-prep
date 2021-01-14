def nodeDepths(root, depth=0):
	if root:
		return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
	return 0

def treeDepth(root, depth=-1):
    #considering root at depth 0; if root is at depth 1, then change to depth=0
    if root:
        return max(treeDepth(root.left, depth+1), treeDepth(root.right, depth+1))
    return depth
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
actual = nodeDepths(root)
print(actual)
depth = treeDepth(root)
print(depth)