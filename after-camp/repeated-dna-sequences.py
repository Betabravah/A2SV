class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        left = 0
        for right in range(min(len(s), 10)):
            right += 1
            
        seen[s[left:right]] = 1
            
        left += 1
        ans = set()
        for i in range(right, len(s)):
            substring = s[left:i+1]
            
            if substring in seen:
                ans.add(substring)
            
            seen[substring] += 1
            left += 1
        
        return ans