class Leaderboard:

    def __init__(self):
        self.score = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.score[playerId] += score

    def top(self, K: int) -> int:
        items = sorted(self.score.items(), key=lambda x: x[1])
        items = items[-K:]
        
        
        
        ans = 0
        for i in items:
            ans += i[1]
            
        return ans

    def reset(self, playerId: int) -> None:
        self.score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)