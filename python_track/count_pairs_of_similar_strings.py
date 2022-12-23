class Solution:
    def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        for i in range(len(words)):
            check = True
            for j in range(i+1, len(words)):
                if Counter(words[i]).keys() == Counter(words[j]).keys():
                    pairs += 1
                
        return pairs
