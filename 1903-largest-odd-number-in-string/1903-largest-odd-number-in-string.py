class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = None
        
        for idx, i in enumerate(num):
            if int(i) % 2 == 1:
                ans = idx
                
                
        return num[:ans+1] if ans != None else ''