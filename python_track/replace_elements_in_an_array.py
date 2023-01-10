class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        _dict = defaultdict(int)
        for idx, num in enumerate(nums):
           _dict[num] = idx
        
        for op in operations:
            oldNum = op[0]
            newNum = op[1]
            idx = _dict[oldNum]
            _dict.pop(oldNum)
            _dict[newNum] = idx

        new = defaultdict(int)
        for key in _dict:
            new[_dict[key]] = key
        nums = [None] * len(new)
        for key in new:
            nums[key] = new[key]

        return nums
   
