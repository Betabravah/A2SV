class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        heaters.sort()
        for i in range(len(houses)):
            minLen = inf
            
            low, high = 0, len(heaters) - 1
            while low <= high:
                
                mid = low + (high - low) // 2
                # print(houses[i], heaters[mid])
                if heaters[mid] > houses[i]:
                    high = mid - 1
                elif  heaters[mid] == houses[i]:
                    minLen = 0
                    break
                else:
                    low = mid + 1
                minLen = min(minLen, abs(heaters[mid] - houses[i]))
                
            
            radius = max(radius, minLen)
            
        return radius
                
                