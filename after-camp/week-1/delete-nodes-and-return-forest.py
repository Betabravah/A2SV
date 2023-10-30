# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def recurse(node, par, is_left):
            nonlocal ans
            
            if not node:
                return
            
            elif node.val in to_delete:
                if par:
                    if is_left:
                        par.left = None
                    else:
                        par.right = None

                recurse(node.left, None, True)
                recurse(node.right, None, False)
                return
            
            if not par:
                ans.append(node)
                
            recurse(node.left, node, True)
            recurse(node.right, node, False)
                
                
        ans = []
        to_delete = set(to_delete)
        recurse(root, None, None)
        return ans