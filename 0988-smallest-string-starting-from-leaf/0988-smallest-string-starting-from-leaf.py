# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:        
        
        def traverse(node, path):
            nonlocal ans
            
            if not node:
                return
            
            if not node.left and not node.right:
                path.append(node.val)
                ans.append(path[::-1])
                        
            traverse(node.left, path + [node.val])
            traverse(node.right, path + [node.val])
            
            
            
        ans = []
        traverse(root, [])
        ans = min(ans)
        res = []
        for i in range(len(ans)):
            res.append(chr(ans[i] + ord('a')))
            
        return ''.join(res)