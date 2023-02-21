# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = head
        if head:
            evens = head.next
        else:
            evens = None
            
        odd, even = odds, evens
        while odd and odd.next and even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        if odd:
            odd.next = evens
        return odds
