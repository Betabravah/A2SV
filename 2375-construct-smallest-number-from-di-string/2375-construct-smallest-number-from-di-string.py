class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        def backtrack(path, prev, idx, visited):
            nonlocal ans
            
            if idx == len(pattern):
                ans.append(''.join(path))
                return
            
            if pattern[idx] == 'I':
                for i in range(prev+1, 10):
                    if i not in visited:
                        visited.add(i)
                        backtrack(path + [str(i)], i, idx+1, visited)
                        visited.remove(i)
                    
            else:
                for i in range(prev-1, 0, -1):
                    if i not in visited:
                        visited.add(i)
                        backtrack(path + [str(i)], i, idx+1, visited)
                        visited.remove(i)
                    
        ans = []            
        for i in range(1, 10):
            backtrack([str(i)], i, 0, set([i]))
        
        
        ans.sort()
        return ans[0]
        
                    
    
                