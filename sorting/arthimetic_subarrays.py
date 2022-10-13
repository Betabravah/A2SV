class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            check = True
            subarray = nums[l[i]:r[i] + 1]
            subarray.sort()
            for j in range(1, len(subarray)):
                if subarray[j] - subarray[j-1] != subarray[1] - subarray[0]:
                    check = False
            answer.append(check)
        
        return answer
