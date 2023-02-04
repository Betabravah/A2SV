#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        minn = arr[i]
        minIdx = i
        while i < len(arr):
            if arr[i] < minn:
                minn = min(minn, arr[i])
                minIdx = i
            i += 1
        return minIdx
    
    def selectionSort(self, arr,n):
        #code here
        i = 0
        while i < len(arr):
            swapIdx = self.select(arr, i)
            arr[i], arr[swapIdx] = arr[swapIdx], arr[i]
            i += 1
        return arr
            
