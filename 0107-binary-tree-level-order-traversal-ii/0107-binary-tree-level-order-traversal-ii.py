# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
        
        def traverse(root, idx):
            if not root:
                return
            
            level[idx] += [root.val]
            traverse(root.left, idx + 1)
            traverse(root.right, idx + 1)
            
            return list(level.values())
    
        answer = traverse(root, 0)
        if answer:
            answer = answer[::-1]
        return answer
        