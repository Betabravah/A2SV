class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        ans1 = set()
        for i in nums1:
            if i not in set2:
                ans1.add(i)
        
        ans2 = set()
        for i in nums2:
            if i not in set1:
                ans2.add(i)
                
                
        return [ans1, ans2]