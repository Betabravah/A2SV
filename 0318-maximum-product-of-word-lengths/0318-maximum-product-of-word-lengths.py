class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        word_mask = []
        for word in words:
            mask = 0
            for char in word:
                order = ord(char) - ord('a')
                
                mask |= 1 << order
                
            word_mask.append(mask)
            
            
        maxLen = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                
                if word_mask[i] & word_mask[j] == 0: # means no duplicates
                    maxLen = max(maxLen, len(words[i]) * len(words[j]))
                    
                    
        return maxLen
        
        