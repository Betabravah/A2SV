class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def generate(path, depth, prev):
            nonlocal ans
            
            if depth == n:
                ans.append("".join(path))
                return
                
            for i in letters:
                if i == prev: continue
                    
                generate(path + [i], depth+1, i)
                
        ans = []
        letters = ['a', 'b', 'c']
        
        generate([], 0, "")
        ans.sort()
        
        return ans[k-1] if len(ans) >= k else ""
                    
            