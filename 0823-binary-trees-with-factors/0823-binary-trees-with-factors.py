class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        
        ans = defaultdict(int)
        
        
        for i in arr:
            temp = 1
            
            for j in arr:
                if j > i:
                    break
                temp += (ans[j] * ans[i/j])
                
            ans[i] = temp
                    
                
        res = 0
        for i in ans:
            res += ans[i]
            
        return res % (10**9 + 7)
        
                
            