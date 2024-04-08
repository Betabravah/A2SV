class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:        
        queue = deque(students)
        
        
        index = 0
        
        while index < len(sandwiches):
            got = False
            length = len(queue)
            
            for i in range(length):
                if queue[0] == sandwiches[index]:
                    index += 1
                    queue.popleft()
                    got = True
                else:
                    front = queue.popleft()
                    queue.append(front)
                    
            if not got:
                return len(queue)
                    
            
        return len(queue)