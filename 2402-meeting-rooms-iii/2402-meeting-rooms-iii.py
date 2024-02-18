class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        rooms = [0] * n
        freeRoom = list(range(n))
        used = []

        for meet in meetings:
            
            while used and used[0][0] <= meet[0]:
                _, room = heappop(used)
                heappush(freeRoom, room)

            start, m_time = meet[0], meet[1] - meet[0]
            if not freeRoom:  # If no free room, get the one that frees up the earliest
                start, room = heappop(used)
            else:
                room = heappop(freeRoom)

            rooms[room] += 1
            heappush(used, (start + m_time, room))

        
        idx = rooms.index(max(rooms))
        return idx
        
        