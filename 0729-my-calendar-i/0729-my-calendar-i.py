class MyCalendar:

    def __init__(self):
        self.events = []
        self.size = 0

    def book(self, start: int, end: int) -> bool:
        self.events.sort()
        
        left, right = 0, len(self.events) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if self.events[mid][0] > start:
                right = mid - 1
                
            elif self.events[mid][0] < start:
                left = mid + 1
            else:
                return False
            
        before = self.events[left-1] if left > 0 else None
        after = self.events[left] if left <= self.size -1 else None
        
        if before and start < before[1]:
            return False
        if after and after[0] < end:
            return False
        
        self.events.append([start, end])
        self.size += 1
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)