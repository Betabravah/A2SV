class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = ans = 0
        count = defaultdict(int)
        

        while right < len(s):
            count[s[right]] += 1
            
            
            while count[s[right]] > 1:
                count[s[left]] -= 1
                
                if count[s[left]] == 0:
                    count.pop(s[left])
                    
                left += 1
                
            ans = max(ans, right - left + 1)
            
            right += 1
            
        return ans