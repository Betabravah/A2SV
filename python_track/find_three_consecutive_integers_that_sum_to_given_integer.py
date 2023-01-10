class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        start = (num-3) / 3
        if start % 1 != 0:
            return []
        else:
            start = int(start)
            return[start, start+1, start+2]
