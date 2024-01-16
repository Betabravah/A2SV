class RandomizedSet:

    def __init__(self):
        self.index = defaultdict(int)
        self.values = []
        self.size = -1
        

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        if self.size < len(self.values) - 1:
            self.values[self.size + 1] = val
        else:
            self.values.append(val)
            
            
        self.size += 1
        self.index[val] = self.size
        
        return True
    
    def remove(self, val: int) -> bool:
        if val in self.index:
            idx = self.index[val]
            
            last_idx = self.size
            last_elem = self.values[last_idx]
            
            self.values[last_idx], self.values[idx] = self.values[idx], self.values[last_idx]
            
            self.index[last_elem] = idx
            
            self.size -= 1
            
            self.index.pop(val)
            return True
        
        return False
            

    def getRandom(self) -> int:
        idx = random.randint(0, self.size)
        return self.values[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()