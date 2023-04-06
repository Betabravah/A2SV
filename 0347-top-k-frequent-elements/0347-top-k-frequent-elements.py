class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        
        ans = []
        for num in count:
            ans.append(num)
            if len(ans) == k:
                break
                
        return ans
            