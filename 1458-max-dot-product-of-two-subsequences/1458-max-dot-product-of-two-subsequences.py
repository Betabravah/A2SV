class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-float(inf)] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        temp = nums1[0] * nums2[0]
            
        
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + nums1[i-1] * nums2[j-1], nums1[i-1] * nums2[j-1], dp[i-1][j], dp[i][j-1]) 
        
        
        return dp[-1][-1]
        
        
    #      3 -2
    #    0 0  0
    #  2 0 6  -4 
    # -6 0 6  18
    #  7 0 21 
        