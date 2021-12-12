def minHeightBst(array):
    return buildMinHeightBST(array, 0, len(array)-1)
    
def buildMinHeightBST(array, left, right):
    if right < left:
        return None
    root_indx = (left+right)//2
    bst = BST(array[root_indx])
    bst.left = buildMinHeightBST(array, left, root_indx-1)
    bst.right = buildMinHeightBST(array, root_indx+1, right)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
