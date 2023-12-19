class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                
                total = count = 0
                
                for k in range(max(0, i-1), min(n, i+2)):
                    for l in range(max(0, j-1), min(m, j+2)):
                        
                        total += img[k][l]
                        count += 1
                        
                ans[i][j] = total // count
                
        return ans