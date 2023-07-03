class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge_sort(start, end):
            if start >= end:
                return 0
            
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid+1, end)
            
            
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] > nums[j] * 2:
                    count += mid - i + 1
                    j += 1
                    
                else:
                    i += 1
                    
                    
            nums[start:end + 1] = sorted(nums[start:end + 1])
            
            return count
        
        return merge_sort(0, len(nums)-1)
                    
            
            