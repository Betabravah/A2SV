from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter(s)
        for letter, count in t_count.items():
            if letter not in s_count:
                return letter
            elif letter in s_count and t_count[letter] != s_count[letter]:
                return letter
