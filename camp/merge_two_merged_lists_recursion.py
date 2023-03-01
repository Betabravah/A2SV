# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = ListNode(0)
        self.cur = self.head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            self.cur.next = list2
            return self.head.next

        if not list2:
            self.cur.next = list1
            return self.head.next
            
        else:
            if list1.val < list2.val:
                self.cur.next = list1
                list1 = list1.next
            else:
                self.cur.next = list2
                list2 = list2.next
            self.cur =  self.cur.next
            return self.mergeTwoLists(list1, list2)
