class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        nums2.sort()
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[j] > nums1[i]:
                    arr.append(nums2[j])
                    break
            if len(arr) < i+1:
                arr.append(-1)
                
        return arr