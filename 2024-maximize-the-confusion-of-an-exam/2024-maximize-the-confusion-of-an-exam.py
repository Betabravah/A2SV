class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = right = 0
        freq = defaultdict(int)
        ans = 0
        
        while right < len(answerKey):
            freq[answerKey[right]] += 1
            
            count = min(freq['T'], freq['F'])
            
            while count > k:
                
                freq[answerKey[left]] -= 1
                count = min(freq['T'], freq['F'])
                
                left += 1
                
            ans = max(ans, right - left + 1)
            
            right += 1
            
        return ans
            
            
        
        