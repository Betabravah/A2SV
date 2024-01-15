class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = defaultdict(int)
        players = set()
        
        
        for i, j in matches:
            lose[j] += 1
            
            players.add(i)
            players.add(j)
        
        
        players = sorted(players)
        
        
        one_loss = []
        never_lost = []
        
        for i in players:
            if not lose[i]:
                never_lost.append(i)
                
            elif lose[i] == 1:
                one_loss.append(i)
                
                
        return [never_lost, one_loss]