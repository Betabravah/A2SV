# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        
        def merge(head1, head2):
            dummy = ListNode(0)
            cur = dummy
            
            while head1 and head2:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
                    
            if head1:
                cur.next = head1
            elif head2:
                cur.next = head2
                
            return dummy.next
                
            
        def split_sort(head):
            tmp = head
            if not tmp:
                return None
            if tmp.next == None:
                return tmp
            fast = slow = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            first, second = head, slow.next
            slow.next = None
            
            res = merge(split_sort(first), split_sort(second))
            return res
                    
    
        return split_sort(head)
            
        
                    
                
        