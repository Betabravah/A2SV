# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        prev = dummy
        next_dig = 0
        
        while l1 or l2:
            num = next_dig
            
            if l1:
                num += l1.val
                l1 = l1.next
                
            if l2:
                num += l2.val
                l2 = l2.next
                
            cur_dig = num % 10
            next_dig = num // 10
            
            next_node = ListNode(cur_dig)
            prev.next = next_node
            prev = next_node
            
            
        if next_dig:
            prev.next = ListNode(next_dig)
            
        return dummy.next
            