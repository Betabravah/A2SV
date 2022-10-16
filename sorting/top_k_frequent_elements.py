from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        count = []
        _dict = Counter(nums)
                
        for num in _dict:
            count.append([num, _dict[num]])

        count.sort(key = lambda x : x[1], reverse=True)
            
        for i in range(k):
            maxElements.append(count[i][0])
        
        return maxElements
