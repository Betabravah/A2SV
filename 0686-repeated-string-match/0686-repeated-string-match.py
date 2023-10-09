class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        pairs = set()
        for i in range(len(a)-1):
            pairs.add((a[i], a[i+1]))
            
        pairs.add((a[-1], a[0]))
        
        for i in range(len(b)-1):
            if (b[i], b[i+1]) not in pairs:
                return -1
            
        
        lps = [0] * len(b)
        prevLps, i = 0, 1
        
        while i < len(b):
            
            if b[i] == b[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
                
            else:
                if prevLps == 0:
                    i += 1
                    
                else:
                    prevLps = lps[prevLps - 1]
                    
        
        
        s_i = n_i = 0
        count = 1
        
        while s_i < len(a):
                
            if count > len(b):
                break
            
            if b[n_i] == a[s_i]:
                s_i += 1
                n_i += 1
                
            elif n_i == 0:
                s_i += 1
                
            else:
                n_i = lps[n_i - 1]
              
            
            if n_i == len(b):
                return count
            
            if s_i >= len(a):
                s_i = s_i % len(a)
                count += 1
            
        return -1