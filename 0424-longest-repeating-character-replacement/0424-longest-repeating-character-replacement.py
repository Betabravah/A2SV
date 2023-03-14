class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        countMax = maxLen = 0

        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            countMax = max(countMax, count[s[right]])

            while (right - left + 1) - countMax > k:
                count[s[left]] -= 1
                left += 1
        
            maxLen = max(maxLen, right-left+1)
        return maxLen


