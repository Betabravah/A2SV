class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        
        s1 = s[:n//2]
        s2 = s[n//2:]
        
        vowel1 = vowel2 = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i in range(n//2):
            if s1[i] in vowels:
                vowel1 += 1
            if s2[i] in vowels:
                vowel2 += 1
                
        return vowel1 == vowel2