class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        ans = 0
        
        for num in nums:
            if num - 1 not in hashmap:
                current_num = num
                length = 1
                
                while current_num + 1 in hashmap:
                    current_num += 1
                    length += 1
                    
                ans = max(ans, length)
        
        return ans