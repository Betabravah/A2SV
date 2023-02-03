class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = arr[-1]

        greatest = [None for _ in range(len(arr))]
        greatest[-1] = -1
        for idx in range(len(arr)-2, -1, -1):
            greatest[idx] = maxRight
            maxRight = max(maxRight, arr[idx])

        return greatest
