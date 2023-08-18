class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']            
        }
        
        ans = []
        def dfs(idx, cur):
            nonlocal ans
            
            if idx >= len(digits):
                if cur:
                    ans.append(cur)
                return
            
            for i in letter[digits[idx]]:                
                dfs(idx+1, cur + i)
                
                
        dfs(0, '')
        return ans