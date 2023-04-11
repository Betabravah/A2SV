"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = {}
        
        for emp in employees:
            emps[emp.id] = emp
        
        
        ans = 0        
        def dfs(emp):
            nonlocal ans

            ans += emp.importance
            
            if not emp.subordinates:
                return 0            
            
            for sub in emp.subordinates:
                sub = emps[sub]
                dfs(sub)
                
        dfs(emps[id])
        return ans
                
            
                
            