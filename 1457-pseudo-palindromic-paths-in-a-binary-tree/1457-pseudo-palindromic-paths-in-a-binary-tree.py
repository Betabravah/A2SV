# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def is_palindrome(count):
            is_odd = False
            
            for i in count:
                if count[i] % 2:
                    if is_odd:
                        return False
                    
                    is_odd = True
                    
            return True
                    
        
        def dfs(node, count):
            nonlocal ans
            
            if not node:
                return
            
            if node.val in count:
                count[node.val] += 1
            else:
                count[node.val] = 1
                
            
            if not node.left and not node.right:
                if is_palindrome(count):
                    ans += 1
                    
            
                    
            dfs(node.left, count)
            dfs(node.right, count)
            
            count[node.val] -= 1
            if count[node.val] == 0:
                count.pop(node.val)
            
        ans = 0
        dfs(root, {})
        return ans