class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        
        ans = float('inf')
        for i in 'balon':
            if i == 'l' or i == 'o':
                ans = min(ans, freq[i] // 2)
            else:
                ans = min(ans, freq[i])
                
        return ans
                