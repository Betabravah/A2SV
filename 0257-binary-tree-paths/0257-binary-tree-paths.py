# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []
        def traverse(root, path):
            if not root:
                path.append(None)
                return
            
            path.append(root.val)
            if not root.left and not root.right:
                all_paths.append(path.copy())
                return 
            
            
            traverse(root.left, path)
            path.pop()
            traverse(root.right, path)
            path.pop()
            
            
        traverse(root, [])
        total_paths = all_paths
        
        answer = []
        for p in total_paths:
            p = map(str, p)
            answer.append('->'.join(p))
        return answer
                
            
            
            