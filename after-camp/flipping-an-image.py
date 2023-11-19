class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        ans = []
        for arr in image:
            arr = arr[::-1]
            
            ans.append([1 if i == 0 else 0 for i in arr])
            
        return ans