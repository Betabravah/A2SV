class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        def calculate_time(garbage, travel, garbage_type):
            travel_cost = 0
            ans = 0
            
            for idx, gar in enumerate(garbage):
                if idx > 0:
                    travel_cost += travel[idx-1]
                    
                for j in gar:
                    if j == garbage_type:
                        ans += 1
                        ans += travel_cost
                        
                        travel_cost = 0
                        
                
                        
            return ans
        
        
        gars = 'GPM'
        res = 0
        for i in gars:
            res += calculate_time(garbage, travel, i)
            
        return res
            
                        
                    
                    
            