class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]

        
        gap = abs(len(x)- len(y))
        if len(x) < len(y):
            x = '0' * gap + x
        else:
            y = '0' * gap + y
            
        
        distance = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                distance += 1
                
        return distance