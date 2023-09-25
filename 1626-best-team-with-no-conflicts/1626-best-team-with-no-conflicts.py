class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        score_age = zip(scores, ages)
        score_age = sorted(score_age)
        
            
        dp = [score_age[i][0] for i in range(len(ages))]
        
        for i in range(len(score_age)):
            mscore, mage = score_age[i]
            
            for j in range(0, i):
                score, age = score_age[j]
                
                if mage >= age:
                    dp[i] = max(mscore + dp[j], dp[i])
                    
                    
        return max(dp)
                    
                    
            
        
        
        