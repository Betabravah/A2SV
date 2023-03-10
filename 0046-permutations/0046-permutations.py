class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        
        visited = set()
        def find(path):
            if len(path) == n:
                permutations.append(path.copy())
                return
            
            for i in range(n):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    find(path)
                    path.pop()
                    visited.remove(nums[i])
            
        find([])
        
        return permutations
            