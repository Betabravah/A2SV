class Solution:
    def balancedString(self, s: str) -> int:
        n, k = len(s), len(s) / 4
        
        left = 0
        count = Counter(s)
        
        ans = inf
        for right in range(n):
            count[s[right]] -= 1
            
            while left < n and count['Q'] <= k and count['W'] <= k and count['E'] <= k and count['R'] <= k:
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1
                
        return ans