class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasibile(speed):
            hour = 0
            for pile in piles:
                hour += ceil(pile / speed)
            print(hour)
            return hour <= h


        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2

            if feasibile(mid):
                right = mid
            else:
                left = mid + 1

        return left

