# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
            
        nums[k-1], nums[-k] = nums[-k], nums[k-1]
        
        
        dummy = ListNode()
        prev = dummy
        
        for i in nums:
            prev.next = ListNode(i)
            prev = prev.next
            
        return dummy.next
            
            
            
        