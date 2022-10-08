class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        for i in range(k):
            if s[i] in "aeiou":
                vowels += 1
        start = 0
        newV = vowels
        for end in range(k, len(s)):
            if s[end] in "aeiou":
                newV += 1
            if s[start] in "aeiou":
                newV -= 1
            start += 1
            vowels = max(vowels, newV)

        return vowels