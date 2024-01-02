class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = defaultdict(set)
        
        cur_row = 0
        nums.sort()
        
        
        for i in nums:
            if i in rows[cur_row]:
                cur_row += 1                
            else:
                cur_row = 0
            
            
            rows[cur_row].add(i)
            
        return rows.values()