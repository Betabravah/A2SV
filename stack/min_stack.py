class MinStack:

    def __init__(self):
        
        self.lst = []

    def push(self, val: int) -> None:
        
        self.lst.append(val)

    def pop(self) -> None:
        
        self.lst.pop()

    def top(self) -> int:
        
        return self.lst[-1]

    def getMin(self) -> int:
        
        min = self.lst[0]
        for i in self.lst:
            if i < min:
                min = i
            
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()