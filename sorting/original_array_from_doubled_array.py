class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        queue = [] # to store the doubles
        result = [] # to store the originals
        for i in changed:
            if len(queue) != 0 and i == queue[0]:
                queue.pop(0)
            else:
                queue.append(2*i)
                result.append(i)
        if len(queue) == 0:
            return result
        return []
