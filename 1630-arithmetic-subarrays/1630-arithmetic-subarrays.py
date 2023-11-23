class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            diff = None
            
            for i in range(len(arr)-1):
                if diff == None:
                    diff = arr[i+1] - arr[i]
                    
                else:
                    if arr[i+1] - arr[i] != diff:
                        return False
                    
            return True
        
        
        ans = []
        m = len(l)
        for i in range(m):
            left, right = l[i], r[i]
            
            cur_nums = nums[left:right+1]
            cur_nums.sort()
            
            ans.append(check(cur_nums))
            
        return ans