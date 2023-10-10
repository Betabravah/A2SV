class ListNode(object):
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seen = {}
        
        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        if key in self.seen:
            node = self.seen[key]
            
            self._remove_node(node)
            self._add_to_head(node)

            
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            node = self.seen[key]
            node.val = value
            self._move_to_head(node)
            
        else:
            if self.capacity == len(self.seen):
                self._remove_last()
                
            new_node = ListNode(key, value)
            self._add_to_head(new_node)
            self.seen[key] = new_node
    
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)
        
    def _remove_node(self, node):
        prev = node.prev
        nextt = node.next
        
        prev.next = nextt
        nextt.prev = prev
        
    def _add_to_head(self, node):
        next_node = self.head.next
        node.next = next_node
        next_node.prev = node
        
        self.head.next = node
        node.prev = self.head
        
    def _remove_last(self):
        last_node = self.tail.prev
        self.seen.pop(last_node.key)
        
        self._remove_node(last_node)
        
        
    
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)