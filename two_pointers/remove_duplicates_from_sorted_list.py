# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        current = head
        
        while current:
            if current.next != None and current.val == current.next.val:
               
                while current.next != None and current.val == current.next.val:
                    current = current.next
                    
                previous.next = current.next
            else:
                previous = previous.next
            
            current = current.next
            
        return dummy.next
