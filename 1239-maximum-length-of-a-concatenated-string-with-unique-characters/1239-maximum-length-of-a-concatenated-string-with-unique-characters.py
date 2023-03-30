class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        maxLen = 0
        letters = defaultdict(int)
        length = 0
        
        def backtrack(idx):
            nonlocal maxLen
            nonlocal length
            
            if idx == len(arr):
                return
            
            curStr = arr[idx]
            count = Counter(curStr)
            for i in count:
                if count[i] > 1:
                    break
            else:
            
                for i in curStr:
                    if letters[i] != 0:
                        break

                else:
                    length += len(curStr)
                    maxLen = max(maxLen, length)

                    for i in curStr:
                        letters[i] += 1

                    backtrack(idx + 1)

                    for i in curStr:
                        letters[i] -= 1
                    length -=  len(curStr)
                
            backtrack(idx + 1)
            
        backtrack(0)
        return maxLen
                    