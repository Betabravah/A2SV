class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        total = 0
        temp = []
        
        for i in range(1, len(heights)):
            
            distance = heights[i] - heights[i - 1] if heights[i] > heights[i-1] else 0
            
            
            if ladders and distance:
                if len(temp) >= ladders:
                    x = heappop(temp)

                    if distance > x:
                        heappush(temp, distance)
                        total += x

                    else:
                        heappush(temp, x)
                        total += distance


                else:
                    heappush(temp, distance)

            else:
                total += distance
                
            if total > bricks:
                    return i - 1


                
        return len(heights) - 1