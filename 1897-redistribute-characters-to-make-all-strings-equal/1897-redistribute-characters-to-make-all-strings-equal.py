class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)
        
        for word in words:
            for i in word:
                count[i] += 1

        for i in count:
            if count[i] % len(words):
                return False
            
        return True