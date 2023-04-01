class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return
        
        def backtrack(idx, curIp, dots):
            if dots == 4 and idx == len(s):
                res.append(curIp[:-1])
                return
            
            if dots > 4:
                return
            
            for j in range(idx, min(idx + 3, len(s))):
                temp = s[idx:j+1]
                if int(temp) < 256 and (idx == j or s[idx] != "0"):
                    backtrack(j + 1, curIp + temp + '.', dots + 1)
                    
        
        res = []
        backtrack(0, '', 0)
        
        return res
        
        