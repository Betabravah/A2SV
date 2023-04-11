class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        primes = set()
        for num in nums:
            
            i = 2
            while i * i <= num:
                while num % i == 0:
                    num //= i
                    primes.add(i)
                    
                i += 1
                
            if num > 1:
                primes.add(num)
                
        return len(primes)
            