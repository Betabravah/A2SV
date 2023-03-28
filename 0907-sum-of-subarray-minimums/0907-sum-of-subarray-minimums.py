class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-inf)
        stack = []
        
        subs = 0
        for i in range(len(arr)):
            
            while stack and arr[stack[-1]] > arr[i]:
            
                idx = stack.pop()
                if stack:
                    prev = stack[-1]
                    subs += arr[idx] * ((idx - prev) * (i - idx))
                else:
                    subs += arr[idx] *((idx+1) * (i - idx))
                
            stack.append(i)
            
        return subs % (10**9 + 7)
            
            
            