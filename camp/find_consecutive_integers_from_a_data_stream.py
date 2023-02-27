class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.lastK = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.lastK -= 1
        else:
            self.lastK = self.k
        if self.lastK > 0:
            return False
        else:
            return True
       




# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
