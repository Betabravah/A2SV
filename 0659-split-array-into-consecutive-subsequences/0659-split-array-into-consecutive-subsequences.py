class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        sequences = []
        
        for num in nums:

            while sequences and sequences[0][0] + 1 < num:
                sub = heappop(sequences)
                if sub[1] < 3:
                    return False

            if not sequences or sequences[0][0] == num:
                heappush(sequences, [num, 1])
                
            else:
                sub = heappop(sequences)
                sub[0] = num
                sub[1] += 1
                heappush(sequences, sub)
                
                
        while sequences:
            sub = heappop(sequences)

            if sub[1] < 3:
                return False
            
        return True
            
            