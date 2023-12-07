from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.score = defaultdict(int)
        self.sorted_score = SortedDict()
        

    def addScore(self, playerId: int, score: int) -> None:
        prev_score = self.score[playerId]
        
        if prev_score:
            self.sorted_score[-prev_score] -= 1
            
            if self.sorted_score[-prev_score] == 0:
                self.sorted_score.pop(-prev_score)
                
            new_score = prev_score + score
            self.sorted_score[-new_score] = self.sorted_score.get(-new_score, 0) + 1
            
        else:
            self.sorted_score[-score] = self.sorted_score.get(-score, 0) + 1
        
        
        self.score[playerId] += score

    def top(self, K: int) -> int:
        ans = 0
        for score, players in self.sorted_score.items():
            possible = min(K, players)
            
            ans += (-score * possible)
            
            K -= possible
            if K == 0:
                break
                
        return ans

    def reset(self, playerId: int) -> None:
        score = self.score[playerId]
        
        self.sorted_score[-score] -= 1
        if self.sorted_score[-score] == 0:
            self.sorted_score.pop(-score)
            
        self.score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)