class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(cap):
            day = 1
            weight = 0
            for i in weights:
                if i > cap:
                    return False
                if weight + i > cap:
                    day += 1
                    weight = 0
                weight += i
            # print(day)
                
            return day <= days
            
            
        low, high = 1, sum(weights)
        while low <= high:
            mid = low + (high - low) // 2

            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1
            
        return low