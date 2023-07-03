class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums.reverse()
        
        temp = []
        answer = []
        
        for num in nums:
            idx = bisect_left(temp, num)
            answer.append(idx)
            temp.insert(idx, num)
            
        answer.reverse()
        return answer