class MinMaxStack:
    """ LIFO (or FILO) and quick access to Min and Max values in the Stack """
    def __init__(self):
        self.stack = []
        self.minMax = []

    def peek(self):
        if self.stack:
            return self.stack[-1]
    def pop(self):
        if self.minMax:
            self.minMax.pop()
        if self.stack:
            return self.stack.pop()
    
    def push(self, number):
        potentialMinMax = {"min":number, "max":number}
        if self.minMax:
            existingMinMax = self.minMax[-1]
            potentialMinMax["min"] = min(existingMinMax["min"], number)
            potentialMinMax["max"] = max(existingMinMax["max"], number)
        self.minMax.append(potentialMinMax)
        self.stack.append(number)
    def getMin(self):
        return self.minMax[-1]['min']
    def getMax(self):
        return self.minMax[-1]['max']
