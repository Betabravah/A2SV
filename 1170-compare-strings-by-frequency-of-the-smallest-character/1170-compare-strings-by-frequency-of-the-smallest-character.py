class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        length = len(words)
        words = sorted(words, key=lambda x: x.count(min(x)))
        words = [[word, word.count(min(word))] for word in words]
        print(words)
        
        greater = [0] * len(queries)
        for i, query in enumerate(queries):
            freq = query.count(min(query))
            
            low, high = 0, len(words) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if words[mid][1] <= freq:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            greater[i] = length - low
        
        
        return greater
            