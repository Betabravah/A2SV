class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        previous = {}
        ctr = 0
        squares = [2**x for x in range(22)]
        for i in range(len(deliciousness)):
            for square in squares:
                diff = square - deliciousness[i]
                if diff in previous:
                    ctr += previous[diff]
            
            previous[deliciousness[i]] = 1 + previous.get(deliciousness[i], 0)
        return ctr % (10**9 + 7)
