class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = str(bin(n)[2:])[::-1]
        
        if len(reversed) < 32:
            reversed += ('0') * (32 - len(reversed))
                    
        return int(reversed, 2)
        