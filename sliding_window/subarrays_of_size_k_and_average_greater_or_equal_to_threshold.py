class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix = ctr = subarrays = 0
        for i in range(k):
            prefix += arr[i]
        
        if prefix / k >= threshold:
            ctr += 1
        
        start = 0
        for end in range(k,len(arr)):
            prefix += arr[end] - arr[start]
            if prefix / k >= threshold:
                ctr += 1
            start += 1
        
        return ctr
       