class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        ans = 0
        for idx, char in enumerate(word):
            if char in vowels:
                ans += ((idx+1) * (len(word) - idx))
                
        return ans