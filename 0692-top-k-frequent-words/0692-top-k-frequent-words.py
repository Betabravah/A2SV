class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        
        for word, cnt in count.items():
            heappush(heap, (-cnt, word))
    
        output = []      
        for i in range(k):
            word = heappop(heap)[1]
            output.append(word)
            
        return output
            
                
