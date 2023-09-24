# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def traverse(node, parent_exists):
            if not node:
                return None
            
            if node.val in to_delete:
                node.left = traverse(node.left, parent_exists=False)
                node.right = traverse(node.right, parent_exists=False)
                return
            
            else:
                if not parent_exists:
                    ans.append(node)
                    
                node.left = traverse(node.left, parent_exists=True)
                node.right = traverse(node.right, parent_exists=True)
                return node
            
        ans = []
        traverse(root, parent_exists=False)
        return ans
                
        