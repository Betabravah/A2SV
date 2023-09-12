class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [None] * len(score)
        index = defaultdict(int)
        
        for i in range(len(score)):
            index[score[i]] = i
            
        score.sort(reverse=True)
        print(score)
        
        for i in range(len(score)):
            
            if i == 0:
                ans[index[score[i]]] = 'Gold Medal'
            elif i == 1:
                ans[index[score[i]]] = 'Silver Medal'
            elif i == 2:
                ans[index[score[i]]] = 'Bronze Medal'
            else:
                ans[index[score[i]]] = str(i + 1)
                
        return ans