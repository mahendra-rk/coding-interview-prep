
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_value=float("-inf"), max_value=float("inf")):
    if tree is None:
        return True
    value = tree.value
    if value < min_value or value >= max_value :
        return False
    return validateBst(tree.left, min_value, value) and validateBst(tree.right, value, max_value)
