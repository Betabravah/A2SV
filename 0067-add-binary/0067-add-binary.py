class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = int(a, 2), int(b, 2)
        
        return bin(num1 + num2)[2:]