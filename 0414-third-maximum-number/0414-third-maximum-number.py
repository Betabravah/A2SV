class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        distinct = []
        
        for num in nums:
            if num not in seen:
                seen.add(num)
                distinct.append(num)
                
        distinct.sort()
        
        return distinct[-3] if len(distinct) >= 3 else distinct[-1]