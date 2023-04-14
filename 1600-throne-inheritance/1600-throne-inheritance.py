class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.hierarchy = defaultdict(list)
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.hierarchy[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def dfs(person):
            children = self.hierarchy[person]
            
            if not children:
                if person not in self.dead:
                    return [person]
                else:
                    return []
            
            cur = [person] if person not in self.dead else []
            
            for child in children:
                cur += dfs(child)
            return cur
        
        return dfs(self.kingName)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()