class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        heap = []
        
        idx1 = idx2 = 0
        total = nums1[idx1] + nums2[idx2]
        
        heappush(heap, [total, idx1, idx2])
        output = []
        seen = set((0, 0))
        
        
        while heap and len(output) < k:

            least = heappop(heap)
            idx1, idx2 = least[1], least[2]
            
            output.append([nums1[idx1], nums2[idx2]])
            
            if (idx1, idx2 + 1) not in seen and idx2 + 1 < m:
                total = nums1[idx1] + nums2[idx2+1]
                heappush(heap, [total, idx1, idx2+1])
                seen.add((idx1, idx2+1))
                
            if (idx1 + 1, idx2) not in seen and idx1 + 1 < n:
                total = nums1[idx1+1] + nums2[idx2]
                heappush(heap, [total, idx1+1, idx2])
                seen.add((idx1+1, idx2))
            
        return output
            
        
        
        