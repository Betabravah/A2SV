# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 0
        
        cur = self.head
        while cur:
            self.n += 1
            cur = cur.next
        

    def getRandom(self) -> int:
        rand = random.randint(0, self.n-1)
        
        cur = self.head
        while rand:
            cur = cur.next
            rand -= 1
            
        return cur.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()