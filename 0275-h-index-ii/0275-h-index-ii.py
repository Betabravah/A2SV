class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        length = len(citations)

        while left <= right:
            mid = (right + left)//2
            pos = bisect_left(citations, mid)
            if mid <= length - pos:
                left = mid + 1
            else:
                right = mid - 1
        return right