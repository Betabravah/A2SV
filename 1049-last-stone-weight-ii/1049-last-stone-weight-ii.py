class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        def recursive(index, sum1, sum2):
            if index >= len(stones):
                return abs(sum1 - sum2)
            
            
            if (sum1, sum2) not in memo[index]:
                diff1 = recursive(index+1, sum1 + stones[index], sum2)
                diff2 = recursive(index + 1, sum1, sum2 + stones[index])
                
                memo[index][(sum1, sum2)] = min(diff1, diff2)
                
            return memo[index][(sum1, sum2)]
        
        memo = [defaultdict(int) for _ in range(len(stones))]
        return recursive(0, 0, 0)