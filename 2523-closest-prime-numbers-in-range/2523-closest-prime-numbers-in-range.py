class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def generatePrime(right):
            isprime = [True for _ in range(right + 1)]
            isprime[0] = isprime[1] = False
            i = 2
            while i * i <= right:
                if isprime[i]:
                    j = i * i
                    while j <= right:
                        isprime[j] = False
                        j += i
                i += 1
            return isprime
        
        
        is_prime = generatePrime(right)
        primes = []
        
        for i in range(left, right+1):
            if is_prime[i]:
                primes.append(i)
                
                
        if len(primes) < 2:
            return [-1, -1]
        
        
        minn = float('inf')
        for i in range(len(primes)-1):
            diff = primes[i+1] - primes[i]
            
            if diff < minn:
                minn = diff
                n1 = primes[i]
                n2 = primes[i+1]
                         
            
            
        return [n1, n2]