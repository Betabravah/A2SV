class Solution:
    def findComplement(self, num: int) -> int:
        compliment = ''
        
        for i in bin(num)[2:]:
            if i == '0':
                compliment += '1'
            else:
                compliment += '0'
                
        return int(compliment, 2)