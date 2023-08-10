class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        
        seen = []
        indices = []
        for i, char in enumerate(s):
            if char in vowels:
                seen.append(char)
                indices.append(i)
        
        s = [i for i in s]        
        for i in range(len(seen)-1, -1, -1):
            s[indices[i]] = seen[len(seen) - 1 - i]
              
        return ''.join(s)

        