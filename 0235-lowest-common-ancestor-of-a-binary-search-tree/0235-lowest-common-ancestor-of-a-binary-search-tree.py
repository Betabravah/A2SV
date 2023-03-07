# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def getmin(root, count=0):
            # if root == p or root == q:
            #     return 1
            # elif root != p and root != q:
            #     return 0
            if not root:
                return False
            
            leftroot = getmin(root.left)
            rightroot = getmin(root.right)
            me = False
            if root.val == p.val or root.val == q.val:
                me = True
            
            if me:
                if leftroot or rightroot:
                    self.ans = root
            else:
                if leftroot and rightroot:
                    self.ans = root
            return me or leftroot or rightroot

        getmin(root)
        
        return self.ans
        