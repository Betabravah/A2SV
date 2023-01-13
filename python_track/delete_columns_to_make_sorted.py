class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ctr = 0
        for col in range(len(strs[0])):
            order = ord(strs[0][col])
            for row in strs:
                newOrd = ord(row[col])
                if newOrd < order:
                    ctr += 1
                    break
                else:
                    order = newOrd
        return ctr
