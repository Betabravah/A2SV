# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in range(len(lists)):
            cur = lists[i]
            
            while cur:
                heappush(heap, cur.val)
                cur = cur.next
        
        
        if not heap: return 
        
        head = ListNode(heappop(heap))
        cur = head
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next
            
        return head
            