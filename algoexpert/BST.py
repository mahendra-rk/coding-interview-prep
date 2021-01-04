class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
			if self.left == None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		elif value >= self.value:
			if self.right == None:
				self.right = BST(value)
			else:
				self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		return True
	
    def remove(self, value, parentNode=None):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			else: # value to delete is found in BST
				if currentNode.left is not None and currentNode.right is not None: # node has 2 children nodes
					currentNode.value = currentNode.right.getMinValue() #replace value with smallest value in right sub tree
					currentNode.right.remove(currentNode.value, parentNode=currentNode)
				elif parentNode is None:#rootnode case; node has no ParentNode & has 1 child node or less
					if currentNode.left is not None: # if LeftChildNode
						currentNode.value = currentNode.left.value ##
						currentNode.right = currentNode.left.right ## Replace value & children of currentNode with value and children of LeftChildNode
						currentNode.left = currentNode.left.left   ## Assign left value last; To avoid overwrite
					elif currentNode.right is not None: # if RightChildNode
						currentNode.value = currentNode.right.value ##
						currentNode.left = currentNode.right.left   ## Replace value & children of currentNode with value and children of RightChildNode
						currentNode.right = currentNode.right.right ## Assign right value last; To avoid overwrite
					else: # if no children 
						currentNode.value = None # removes the single remaining node in the tree
				elif parentNode.left == currentNode: # check if node to be removed is LeftChildNode of Parent
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right # Assign LeftChildNode(if no LCN then assign RightChildNode) of NodeToBeRemoved to ParentNode
				elif parentNode.right == currentNode: # check if node to be removed is RightChildNode of Parent
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right # Assign LeftChildNode(if no LCN then assign RightChildNode) of NodeToBeRemoved to ParentNode					
				break	
        return self
	
	
	def getMinValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMinValue()
	
	
	
	
	
	
	
	
	
	
	
	
