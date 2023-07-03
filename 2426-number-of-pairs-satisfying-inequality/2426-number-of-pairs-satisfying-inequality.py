class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        def merge_sort(nums):
            if len(nums) <= 1: return 0
            
            
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            countl = merge_sort(left)
            countr = merge_sort(right)
            
            
            i = j = count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    count += (len(right) - j)
                    i += 1
                else:
                    j += 1
                    
                    
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    
                k += 1
                
                
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
                
        
            return countl + countr + count
        
        nums = [a - b for (a, b) in zip(nums1, nums2)]
        return merge_sort(nums)
            
            