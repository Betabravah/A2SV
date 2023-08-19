class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        
        ans = []
        for num in freq:
            if freq[num] > len(nums) // 3:
                ans.append(num)
                
        return ans