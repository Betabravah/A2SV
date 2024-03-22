# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = prev = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        prev = ListNode()
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        
        cur1 = head
        cur2 = prev
        
        while cur1 and cur2:
            print(cur1.val, cur2.val)
            if cur1.val != cur2.val:
                return False
            
            cur1 = cur1.next
            cur2 = cur2.next
            
        return True
            
            
            