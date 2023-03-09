class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def backtrack(state, idx):
            if idx == len(cookies):
                return max(state)
            
            unfairness = float('inf')
            for j in range(k):
                state[j] += cookies[idx]
                if state[j] > unfairness:
                    state[j] -= cookies[idx]
                    continue
                distribute = backtrack(state, idx+1)
                state[j] -= cookies[idx]
                unfairness = min(unfairness, distribute)
            return unfairness
        
        return backtrack([0]*k, 0)