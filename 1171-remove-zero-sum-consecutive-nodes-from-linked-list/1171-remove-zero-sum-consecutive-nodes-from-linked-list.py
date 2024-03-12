# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        sum_to_node = {0: dummy}

        
        cur = head
        while cur:
            prefix_sum += cur.val
            sum_to_node[prefix_sum] = cur
            cur = cur.next
        
        
        prefix_sum = 0
        cur = dummy
        while cur:
            prefix_sum += cur.val
            cur.next = sum_to_node[prefix_sum].next
            cur = cur.next
        
        return dummy.next