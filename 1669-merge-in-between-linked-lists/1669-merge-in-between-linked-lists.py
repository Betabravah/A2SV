# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode()
        dummy.next = list1
        prev = dummy
        cur = list1
        got = False
        ctr = 0
        
        while cur:
            if ctr == a:
                got = True
            
            if ctr == b:
                last = cur.next
                break
    
            cur = cur.next
        
            if not got:
                prev = prev.next
            
            ctr += 1
            
                
        prev.next = list2
        
        cur = list2
        while cur:
            cur = cur.next
            prev = prev.next
            
        prev.next = last
        
        return dummy.next
        
        
                
                