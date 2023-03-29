class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        
        count = defaultdict(int)
        self.leader = []
        cur_leader = [persons[0], 1]
        
        for p in persons:
            count[p] += 1
            
            if cur_leader[1] <= count[p]:
                cur_leader = [p, count[p]]
                
            self.leader.append(cur_leader[0])
        
        

    def q(self, t: int) -> int:
        low, high = 0, len(self.times) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if self.times[mid] < t:
                low = mid + 1
            elif self.times[mid] > t:
                high = mid - 1
            else:
                low = mid + 1
                break
                
                
        return self.leader[low - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)