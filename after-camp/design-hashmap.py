class MyHashMap:

    def __init__(self):
        self.arr = [None] * (10 ** 6 + 1)
        

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value
        

    def get(self, key: int) -> int:
        if self.arr[key] != None:
            return self.arr[key]
        return -1
        

    def remove(self, key: int) -> None:
        self.arr[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)