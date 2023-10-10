class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powered = {0:1}
        def compute_power(i):
            for j in range(1, i):
                powered[j] = powered[j-1] * power
                
        compute_power(k)
        
        
        def char_order(char):
            
            return ord(char) - ord('a') + 1
            
        
        
        def add_last(num, char):
            num = num * power
            num = (num + char_order(char)) % modulo
            return num
        
        
        def poll_first(num, char, index):
            num = (num - (char_order(char) * powered[index])) % modulo
            return num
            
        
        if len(s) < k:
            return -1
            
        hhash = 0
        i = len(s)-1
        
        while len(s)-1 - i < k:
            hhash = add_last(hhash, s[i])
            
            i -= 1
        
        right = len(s) - 1
        while i > -1:
            if hhash == hashValue:
                ans = s[i+1:i+1+k]
            
            
            hhash = poll_first(hhash, s[right], k-1)
            hhash = add_last(hhash, s[i])
            
            
            i -= 1
            right -= 1
        
        if hhash == hashValue:
            ans = s[i+1:i+1+k]
        
        return ans if ans else -1