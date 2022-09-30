class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLen = 0
        for end in range(len(s)):
            if s[end] in s[start:end]:
                while s[start] != s[end]:
                    start += 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen
