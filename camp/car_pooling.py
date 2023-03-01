class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 10002

        for trip in trips:
            passengers, fromm, to = trip
            prefix[fromm + 1] += passengers
            prefix[to + 1] -= passengers

        for i in range(1, 1002):
            prefix[i] += prefix[i - 1] 
            if prefix[i] > capacity:
                return False
        return True
