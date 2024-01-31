class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        
        stack = []
        
        for idx, i in enumerate(temperatures):
            if stack:
    
                while stack and stack[-1][0] < i:
                    _, prev = stack.pop()

                    ans[prev] = idx - prev

                        
                        
            stack.append([i, idx])
                
                
        return ans
                    
