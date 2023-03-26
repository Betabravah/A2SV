class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left, right = 0, len(arr)-1
        
        
        while left < right:
            notMountl = True
            notMountr = True
            if arr[left+1] > arr[left]:
                notMountl = False
                left += 1
            if arr[right-1] > arr[right]:
                notMountr = False
                right -= 1
            if (notMountl and notMountr) and left < right:
                return False
        if (right < len(arr) -1) and (left > 0):
            return True
        else:
            return False