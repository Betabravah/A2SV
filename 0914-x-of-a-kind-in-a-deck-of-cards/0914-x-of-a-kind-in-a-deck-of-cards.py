class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count = defaultdict(int)
        
        for num in deck:
            count[num] += 1
        
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        
        values = list(count.values())
        divisor = values[0]
        
        for cnt in values:
            divisor = gcd(divisor, cnt)
            
        return divisor > 1