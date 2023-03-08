# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = defaultdict(list)
    def levelOrder(self, root: Optional[TreeNode], first=True) -> List[List[int]]:
        if root:
            self.answer[0] = [root.val]
        
        def get_next_level(root, count):
            if not root:
                return
            if root.left and root.right:
                self.answer[count] += [root.left.val, root.right.val]
            elif root.left:
                self.answer[count] += [root.left.val]
            elif root.right:
                self.answer[count] += [root.right.val]
                
            get_next_level(root.left, count + 1)
            get_next_level(root.right, count + 1)
            
        get_next_level(root, 1)
        
        return self.answer.values()
                