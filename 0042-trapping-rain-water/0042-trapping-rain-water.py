class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        stack=[]
        
        
        for r, x in enumerate(height):
            while stack and height[stack[-1]] < x:
                m = stack[-1]
                stack.pop()
                
                if not stack: break
                    
                l = stack[-1]
                h = min(x, height[l]) - height[m]
                w = r - l - 1
                ans += h*w
            
            stack.append(r)
        return ans
        