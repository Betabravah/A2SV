class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        zeros = 0
        negatives = []
        positives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros += 1
        
        n, p = set(negatives), set(positives)
        ans = set()
        if zeros:
            if zeros > 2:
                ans.add((0, 0, 0))
        
            for num in positives:
                if -num in negatives:
                    ans.add((-num, 0, num))
                    
                    
        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                target = -(negatives[i] + negatives[j])
                
                if target in p:
                    ans.add(tuple(sorted([negatives[i], negatives[j], target])))
                    
        for i in range(len(positives)):
            for j in range(i+1, len(positives)):
                target = -(positives[i] + positives[j])
                
                if target in n:
                    ans.add(tuple(sorted([positives[i], positives[j], target])))
                    
                    
        return ans
                    
        
                    
                    
        
        