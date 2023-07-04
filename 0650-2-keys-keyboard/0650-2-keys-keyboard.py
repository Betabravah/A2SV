class Solution:
    def minSteps(self, n: int) -> int:
        memo = defaultdict(int)
        
        def dp(screen, clipboard):
            
            if (screen, clipboard) in memo: return memo[(screen, clipboard)]
            if screen == n: return 0
            if screen > n: return float('inf')

            
            copy_paste = dp(screen + screen, screen) + 2
            paste = float('inf')
            
            if clipboard:
                paste = dp(screen + clipboard, clipboard) + 1
            
            memo[(screen, clipboard)] = min(copy_paste, paste)
            
            return memo[(screen, clipboard)]
        
        return dp(1, 0)
            
            