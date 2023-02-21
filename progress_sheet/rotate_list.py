# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        left = right = head
        length = 1
        while right and right.next:
            right = right.next
            length += 1
        
        right.next = left
        k = length - k % (length)
        if k > 0:
            while k > 1:
                left = left.next
                k -= 1
            right = left.next
            left.next = None
        else:
            right.next = None
            return left

        return right
