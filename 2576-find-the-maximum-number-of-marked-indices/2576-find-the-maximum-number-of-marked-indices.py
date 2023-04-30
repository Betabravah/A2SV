# class Solution:
#     def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        
        
#         # ctr = 2
        
#         # [9,2,5,4]
        
#         # 2, 4,
#         # 5, 9
        
#         # l  r
        
#         # [3,5,2,4]
        
#         # 2, 3, 4, 5, 6, 8, 9
#         #          l        r
        
        
        
#         nums.sort()
        
#         left, right = 0 , len(nums) // 2
        
#         ctr = 0
#         marked = set()
        
#         while right < len(nums):
            
#             if nums[right] >= nums[left] * 2 and left not in marked:
#                 ctr += 2
#                 left += 1
#                 right += 1
#                 marked.add(right)
                
#             else:
#                 right += 1
                
                
#         return ctr

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)//2
        count = 0
        visited = set()
        for j in range(r,len(nums)):
            if  (2*nums[l]<=nums[j]) and (l not in visited):
                count +=2
                l+=1
                visited.add(j)
        return count
                
            
        
        
                
                    
            
                    
            
                    
            
                    
                    
                    
                    
                    
                    
                    
                
        
        
        
        