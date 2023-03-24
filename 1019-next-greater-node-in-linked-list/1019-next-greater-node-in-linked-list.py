# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        
        greater = []
        i = 0
        while head:
            while stack and head.val > stack[-1][0]:
                _, idx = stack.pop()
                greater[idx] = head.val
                
            stack.append([head.val, i])
            greater.append(0)
            i += 1
            head = head.next
            
        return greater
                
                
        