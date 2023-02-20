# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        behind = dummy
        ahead = head
        while n > 0:
            ahead = ahead.next
            n -= 1

        while ahead:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return dummy.next
