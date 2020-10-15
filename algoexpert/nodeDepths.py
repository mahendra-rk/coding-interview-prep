def nodeDepths(root, multiplier=0):
	if root:
		return multiplier + nodeDepths(root.left, multiplier+1) + nodeDepths(root.right, multiplier+1)
	else:
		return 0

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        