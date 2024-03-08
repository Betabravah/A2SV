class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        
        count = defaultdict(list)
        
        for i in freq:
            count[freq[i]].append(i)
            
            
            
        ans = []
        max_count = 0
        for i in count:
            if i > max_count:
                ans = count[i]
                max_count = i
                
        
        res = 0
        for i in ans:
            res += freq[i]
            
        return res
        
                
                
                
            