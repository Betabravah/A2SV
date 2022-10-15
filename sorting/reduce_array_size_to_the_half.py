class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        size = 0
        _dict = {}
        for i in arr:
            if i in _dict.keys():
                _dict[i] += 1
            else:
                _dict[i] = 1
                
        halfLength = len(arr)/2
        counts = sorted(_dict.values(), reverse=True)
        
        for i in counts:
            if count < halfLength:
                count += i
                size += 1
            else:
                break
        return size
