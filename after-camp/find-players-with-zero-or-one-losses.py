class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        for match in matches:
            winner = match[0]
            loser = match[1]
            win[winner] = 1 + win.get(winner, 0)
            lose[loser] = 1 + lose.get(loser, 0)

        noLose = []
        for player in win:
            if player not in lose:
                noLose.append(player)

        oneLose = []
        for player in lose:
            if lose[player] == 1:
                oneLose.append(player)
        
        noLose.sort()
        oneLose.sort()
        return [noLose, oneLose]
        