class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = {0: 'qwertyuiop', 1: 'asdfghjkl', 2: 'zxcvbnm'}
        
        row = {}
        for i in 'qwertyuiop':
            row[i] = 0
            
        for i in 'asdfghjkl':
            row[i] = 1
            
        for i in 'zxcvbnm':
            row[i] = 2
        
        ans = []
        for word in words:
            cur = row[word[0].lower()]
            for char in word:
                if row[char.lower()] != cur:
                    break
            else:
                ans.append(word)
                
        return ans