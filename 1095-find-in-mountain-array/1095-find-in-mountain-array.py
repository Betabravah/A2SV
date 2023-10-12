# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
            
        def get_peak():
            low, high = 0, n - 1

            while low <= high:
                mid = low + (high - low) // 2

                mid_element = mountain_arr.get(mid)
                next_element = mountain_arr.get(mid+1)
                
                
                if mid_element < next_element:
                    low = mid + 1

                elif mid_element > next_element:
                    high = mid - 1
                
            return low
        
        
        
        def search_left(low, high, target):
            
            while low <= high:
                mid = low + (high - low) // 2
                
                mid_element = mountain_arr.get(mid)
                
                if mid_element > target:
                    high = mid - 1
                    
                elif mid_element < target:
                    low = mid + 1
                    
                else:
                    return mid
            
            return -1
        
        def search_right(low, high, target):
            
            while low <= high:
                mid = low + (high - low) // 2
                
                mid_element = mountain_arr.get(mid)
                
                if mid_element < target:
                    high = mid - 1
                    
                elif mid_element > target:
                    low = mid + 1
                    
                else:
                    return mid
            
            return -1
                
            
        n = mountain_arr.length()
        peak_index = get_peak()
        
        ans = search_left(0, peak_index, target)
        if ans != -1:
            return ans
        
        ans = search_right(peak_index+1, n-1, target)
        return ans
        
        
        
                
                
        