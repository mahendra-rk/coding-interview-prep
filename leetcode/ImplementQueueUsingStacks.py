# Leetcode
# 232. Implement Queue using Stacks
class MyQueue:

    ############################################################
    # insert(0, element) can be replaced by append(element)
    # pop(0) can be replaced by pop(), which defaults to pop(-1)
    ############################################################
    def __init__(self):
        self.primary = []
        self.secondary = []
        

    def push(self, x: int) -> None:
        """ Enqueue heavy approach """
        while self.primary:
            # pop all the elements in primary 
            element = self.primary.pop(0)
            # insert into secondary; Elements are inserted in reverse order
            self.secondary.insert(0, element)
        #insert the new element
        self.secondary.insert(0, x)
        while self.secondary:
            # pop all elements in secondary 
            element = self.secondary.pop(0)
            # insert into primary; Elements are inserted in correct order. 
            self.primary.insert(0, element)


    def pop(self) -> int:
        if self.primary:
            return self.primary.pop(0)
        

    def peek(self) -> int:
        if self.primary:
            return self.primary[0]
        

    def empty(self) -> bool:
        return not len(self.primary)
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()