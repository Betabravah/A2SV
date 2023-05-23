# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [[root, 0]]
        col_count = defaultdict(list)
        
        
        while queue:
            temp = queue
            queue = []
            
            length = len(temp)
            
            for i in range(length):
                cur, idx = temp[i]
                
                col_count[idx].append(cur.val)
                
                if cur.left:
                    queue.append([cur.left, idx-1])
                    
                if cur.right:
                    queue.append([cur.right, idx+1])
                    
                    
            queue.sort(key=lambda x:(x[1], x[0].val))
            

        ans = []
        for i in sorted(col_count):
            ans.append(col_count[i])


        return ans
