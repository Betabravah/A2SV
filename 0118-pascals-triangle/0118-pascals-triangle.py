class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]
        if numRows == 1:
            return ans
        
        else:
            for i in range(1, numRows):
                temp = [1] * (i+1)
                for j in range(1, i):
                    temp[j] = ans[-1][j-1] + ans[-1][j]
                    
                ans.append(temp)
                
            return ans
                    