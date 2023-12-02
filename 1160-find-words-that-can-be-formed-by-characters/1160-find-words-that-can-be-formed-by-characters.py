class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        ans = 0
        letters = Counter(chars)
        
        for word in words:
            word_count = Counter(word)
            
            for i in word_count:
                if i in letters and letters[i] >= word_count[i]:
                    pass
                else:
                    break
                    
            else:
                ans += len(word)
                
                
                    
        return ans