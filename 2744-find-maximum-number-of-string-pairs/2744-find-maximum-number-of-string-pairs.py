class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ctr = 0
        reversed = defaultdict(int)
        
        for word in words:
            rev = word[::-1]
            ctr += reversed[rev]
            reversed[word] += 1
            
                
        return ctr