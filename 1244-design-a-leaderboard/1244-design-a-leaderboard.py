from sortedcontainers import SortedList
class Leaderboard:

    def __init__(self):
        self.score = defaultdict(int)
        self.sorted_score = SortedList()
        

    def addScore(self, playerId: int, score: int) -> None:
        prev_score = self.score[playerId]
        if prev_score:
            self.sorted_score.remove(-prev_score)
        
        new_score = prev_score + score
        self.sorted_score.add(-new_score)
        
        self.score[playerId] += score

    def top(self, K: int) -> int:
        ans = 0
        
        for i in range(K):
            ans += self.sorted_score[i]
            
        return -ans

    def reset(self, playerId: int) -> None:
        prev_score = self.score[playerId]
        self.sorted_score.remove(-prev_score)
        
        self.score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)