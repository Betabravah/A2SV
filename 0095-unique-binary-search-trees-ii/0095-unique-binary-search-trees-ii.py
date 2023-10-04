from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generateTreesHelper(start, end):
            result = []

            if start > end:
                result.append(None)
                return result

            for i in range(start, end + 1):
                left_subtrees = generateTreesHelper(start, i - 1)
                right_subtrees = generateTreesHelper(i + 1, end)

                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(i)
                        root.left = left_subtree
                        root.right = right_subtree
                        result.append(root)

            return result

        return generateTreesHelper(1, n)