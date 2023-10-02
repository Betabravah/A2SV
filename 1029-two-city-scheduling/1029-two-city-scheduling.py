class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [[costs[i][0] - costs[i][1], i] for i in range(len(costs))]
        diff.sort(key=lambda x: x[0])
        
        ans = 0
        for i in range(len(costs) // 2):
            index1 = diff[i][1]
            index2 = diff[len(diff)-1-i][1]
            
            
            ans += (costs[index1][0] + costs[index2][1])
            
        return ans
            