# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if not root:
                return []
            else:
                return traverse(root.left) + [root.val] + traverse(root.right)
            
        elements = traverse(root)
        counter = Counter(elements)
        freq = max(list(counter.values()))
        modes = [k for k, v in counter.items() if v == freq]
        return modes