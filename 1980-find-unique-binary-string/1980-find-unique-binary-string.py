class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        seen = set(nums)
        
        
        def backtrack(n, path):
            if n == 0:
                cur = ''.join(path)
                
                if cur not in seen:
                    return cur
                
                return 
            
            ans = backtrack(n-1, path + ['0'])
            if ans:
                return ans
            
            ans = backtrack(n-1, path + ['1'])
            if ans:
                return ans
            
        return backtrack(n, [])
                