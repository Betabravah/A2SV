# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
            
        summ = str(int(''.join(num1)) + int(''.join(num2)))
        
        
        dummy = ListNode(0)
        prev = dummy
        
        for i in summ:
            cur = ListNode(int(i))
            prev.next = cur
            prev = cur
        
        return dummy.next
            
        
        
            
        