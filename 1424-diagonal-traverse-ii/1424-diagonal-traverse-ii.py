class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diag[i+j].append(nums[i][j])
                
        
        ans = []
        for i in range(len(diag)):
            ans += diag[i][::-1]
            
        return ans
            