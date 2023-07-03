from sortedcontainers import SortedList 

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        count = 0
        
        for idx, num in enumerate(instructions):
            idx1, idx2 = nums.bisect_left(num), nums.bisect_right(num)
            
                
            count += min(idx1, idx - idx2)
            nums.add(num)
            
        return count % (10**9 + 7)
            