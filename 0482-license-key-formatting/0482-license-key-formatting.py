class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        
        
        first = len(s) % k
        ans = s[:first]
        
        for i in range(first, len(s), k):
            ans += "-" + s[i:i+k]
        
        
        if not ans:
            return ""
        elif ans[0] == "-":
            return ans[1:]
        else:
            return ans
            
        