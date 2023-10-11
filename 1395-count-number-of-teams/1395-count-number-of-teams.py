class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        @cache
        def dp(idx, used, inc):
            res = 0
            
            if used == 3:
                return 1
            
            for i in range(idx+1, len(rating)):
                if inc:
                    if rating[i] > rating[idx]:
                        res += dp(i, used+1, inc)
                        
                else:
                    if rating[i] < rating[idx]:
                        res += dp(i, used+1, inc)
                        
            return res
        
        ans = 0
        for i in range(len(rating)):
            ans += dp(i, 1, True)
            ans += dp(i, 1, False)
              
        return ans
                
                    
            
                
                    
                
            
            
            