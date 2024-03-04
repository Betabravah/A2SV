class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        
        left, right = 0, n - 1
        score = 0
        ans = 0
        
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
                
                
            elif score:
                score -= 1
                power += tokens[right]
                right -= 1
                
                
            else:
                left += 1
                right -= 1
                
            ans = max(ans, score)
                
                
        return ans
                
                
                
                