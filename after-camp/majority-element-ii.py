class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minn = len(nums) // 3
        freq = Counter(nums)
        
        ans = []
        for i in freq:
            if freq[i] > minn:
                ans.append(i)
                
        return ans