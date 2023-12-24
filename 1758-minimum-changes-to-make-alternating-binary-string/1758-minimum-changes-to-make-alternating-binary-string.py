class Solution:
    def minOperations(self, s: str) -> int:
        chars = [i for i in s]
        
        # start with 0
        ans1 = 0
        if chars[0] != '0':
            ans1 += 1
            chars[0] = '0'
            
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                if chars[i] == '0':
                    chars[i] = '1'
                else:
                    chars[i] = '0'
                    
                ans1 += 1
        
                    
        chars = [i for i in s]
        # start with 1
        ans2 = 0
        if chars[0] != '1':
            ans2 += 1
            chars[0] = '1'
            
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                if chars[i] == '0':
                    chars[i] = '1'
                else:
                    chars[i] = '0'
                    
                ans2 += 1
                
        return min(ans1, ans2)
                
            