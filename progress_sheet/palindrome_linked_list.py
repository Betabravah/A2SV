# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _list = []
        rev = []
        current = head
        while current:
            _list.append(current.val)
            rev.append(current.val)
            current = current.next
        rev.reverse()
        if rev == _list:
            return True
        return False
