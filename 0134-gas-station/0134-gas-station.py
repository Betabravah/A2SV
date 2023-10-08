class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        ans = 0
        total_gas = 0
        current_gas = 0
        
        for i in range(len(gas)):
            total_gas += (gas[i] - cost[i])
            current_gas += (gas[i] - cost[i])
            
            if current_gas < 0:
                ans = i + 1
                current_gas = 0
                
            
        return (ans) % len(gas) if total_gas >= 0 else -1
        
        