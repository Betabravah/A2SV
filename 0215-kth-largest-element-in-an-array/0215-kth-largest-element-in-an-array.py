class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(i, j):
            pivot = nums[i]
            read = write = i + 1
            
            while read <= j:
                if nums[i] > nums[read]:
                    nums[read], nums[write] = nums[write], nums[read]
                    
                    write += 1
                    
                read += 1
                
            nums[i], nums[write-1] = nums[write-1], nums[i]
            return write-1
        
        i, j = 0, len(nums) - 1
        pivot = quick(i, j)
        while len(nums) - pivot != k and i != j:
            
            
            if pivot < len(nums) - k:
                i = pivot + 1
                pivot = quick(i, j)
            elif pivot > len(nums) - k:
                j = pivot - 1
                pivot = quick(i, j)
            else:
                break
            # pivot = quick(i, j)
                
        return nums[pivot]
            