class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        seen = []
        consonant = [False] * len(s)
        
        
        for idx, i in enumerate(s):
            if i in vowels:
                seen.append(i)
                
            else:
                consonant[idx] = True
        
        
        seen.sort()
        prev = 0
        ans = []
        
        for i in range(len(s)):
            if not consonant[i]:
                ans.append(seen[prev])
                prev += 1
            else:
                ans.append(s[i])
                
        return ''.join(ans)
        
        