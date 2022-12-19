class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        isBroken = False
        minString = len(min(strs, key=len))
        for i in range(minString):
            for item in strs:
                if item[i] != strs[0][i]:
                    isBroken = True
                    break
            else:
                ans += strs[0][i]
            if isBroken:
                break
        return ans
