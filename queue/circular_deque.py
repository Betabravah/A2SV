class MyCircularDeque:

    def __init__(self, k: int):
        self.lst = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.lst) < self.k:
            self.lst = [value] + self.lst
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.lst) < self.k:
            self.lst += [value]
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.lst:
            self.lst.pop(0)        
            return True
        return False
    

    def deleteLast(self) -> bool:
        if self.lst:
            self.lst.pop()
            return True
        return False
        

    def getFront(self) -> int:
        if self.lst:
            return self.lst[0]
        return -1

    def getRear(self) -> int:
        if self.lst:
            return self.lst[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.lst:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.lst) == self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()