# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head and head.next:
            while head and head.next and head.val == head.next.val:
                head = head.next
            prev.next = head
            prev, head = prev.next, head.next
        return dummy.next
