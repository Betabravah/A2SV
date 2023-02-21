# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        cur = head.next if head else None
        
        while cur:
            if cur.val < prev.val:
                left = dummy
                prev.next = cur.next
                while left.next and left.next.val < cur.val:
                    left = left.next
                cur.next = left.next
                left.next = cur
                cur = prev.next
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
