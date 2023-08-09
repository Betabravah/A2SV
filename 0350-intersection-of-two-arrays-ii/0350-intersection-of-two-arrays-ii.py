class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        
        ans = []
        for i in freq1:
            if i in freq2:
                ans += [i] * min(freq1[i], freq2[i])
                
        return ans