# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit1 = l1
        digit2 = l2

        dummy = ListNode()
        ptr = dummy
        tmp = 0
        while digit1 or digit2 or tmp:
            if digit1 and digit2:
                sum = digit1.val + digit2.val
                digit1 = digit1.next
                digit2 = digit2.next
            elif digit1:
                sum = digit1.val
                digit1 = digit1.next
            elif digit2:
                sum = digit2.val
                digit2 = digit2.next
            else:
                sum = 0

            if tmp:
                sum += tmp
            num = sum % 10
            tmp = sum // 10
            ptr.next = ListNode(num)
            ptr = ptr.next
        
        return dummy.next
