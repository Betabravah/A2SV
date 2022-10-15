class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        placed = len(arr)
        while arr != sorted(arr):
            
            if max(arr[:placed]) == arr[0]: # flip it and make it last
                flips.append(placed)
                arr[:placed] = arr[placed-1::-1]
                
            elif max(arr[:placed]) != arr[placed-1]: # bring it to index 0 and flip it to make it last
                index = arr.index(max(arr[:placed])) + 1
                flips.append(index)
                arr[:index] = arr[index-1::-1]
                flips.append(placed)
                arr[:placed] = arr[placed-1::-1]
                
            placed -= 1
            
        return flips
