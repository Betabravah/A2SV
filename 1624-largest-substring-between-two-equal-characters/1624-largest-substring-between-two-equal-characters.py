class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_idx = defaultdict(int)
        ans = -1
        
        for idx, i in enumerate(s):
            if i in first_idx:
                ans = max(ans, idx - first_idx[i] - 1)
                
            else:
                first_idx[i] = idx
                
        return ans