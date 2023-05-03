class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = defaultdict(list)
        
        
        self.graph = defaultdict(list)
        
        for i, p in enumerate(parent):
            self.graph[p].append(i)
            
            
        

    def lock(self, num: int, user: int) -> bool:
        
        if not self.locked[num]:
            self.locked[num].append(user)
            return True
        
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        
        if self.locked[num] and self.locked[num][0] == user:
            self.locked[num].pop()
            return True
        
        return False
            
        
    def is_locked(self, num: int) -> bool:
        
        return self.locked[num] != []
    
    
    def upgrade(self, num: int, user: int) -> bool:
        
        if self.is_locked(num):
            return False
        
        cur = num
        while cur != -1: # check for locked ancestor
            if self.is_locked(self.parent[cur]):
                return False
            
            cur = self.parent[cur]
            
            
            
        stack = [num]
        descendants = []
        
        while stack: 
            cur = stack.pop()
            
            
            for neigh in self.graph[cur]:

                if self.is_locked(neigh):
                    descendants.append(neigh)
                    
                stack.append(neigh)
                
                
        if descendants:
            self.locked[num].append(user)

            for i in descendants:
                self.locked[i] = []

            return True
        return False
                
            
                
        
            
            
                
                
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)