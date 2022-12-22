class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        indices = {}
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            if x1 == x or y1 == y:
                distance = abs(x1-x) + abs(y1-y)
                indices[str(i)] = distance
        if indices:
            temp = min(indices.values())
            keys = [int(key) for key in indices if indices[key] == temp]
            return min(keys)
        else:
            return -1
