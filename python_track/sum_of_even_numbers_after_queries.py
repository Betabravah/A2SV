class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in nums:
            if num % 2 == 0:
                evenSum += num
        
        
        evens = []
        even = evenSum
        for query in queries:
            idx = query[1]
            add = query[0]
            newNum = nums[idx] + add
            
            if newNum % 2 == 0:
                if nums[idx] % 2 == 0:
                    even = even + newNum - nums[idx]
                else:
                    even += newNum
            else:
                if nums[idx] % 2 == 0:
                    even -= nums[idx]
                    
            nums[idx] = newNum
            evens.append(even)

        return evens

