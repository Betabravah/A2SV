class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = str(int(''.join(map(str, digits))) + 1)
        
        return [int(i) for i in num]