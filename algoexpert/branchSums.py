class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, sum=0, sumsList=None):
    if root is None:
		return
	if sumsList is None: #refer https://stackoverflow.com/a/60202340/6699913
		sumsList = []
	sum += root.value
	if root.left is None and root.right is None:
		sumsList.append(sum)
	branchSums(root.left, sum, sumsList)
	branchSums(root.right, sum, sumsList)
	return sumsList
