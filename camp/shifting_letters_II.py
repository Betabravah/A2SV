class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for shift in shifts:
            start, end, direction = shift
            if direction == 1:
                arr[start] += 1
                arr[end + 1] -= 1
            else:
                arr[start] -= 1
                arr[end + 1] += 1
        
        prefix = 0
        for i in range(len(arr) - 1):
            prefix += arr[i]
            arr[i] = prefix
        
        shifted = []
        for idx in range(len(arr) - 1):
            char = ord(s[idx])
            order = ((char + arr[idx] - 97) % 26) + 97
            
            shifted.append(chr(order))
        
        
        return ''.join(shifted)
