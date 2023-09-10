# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = prev.next
                
                
            cur = cur.next
        
        prev.next = None
        return dummy.next if dummy != prev else prev.next
        