class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = maxSum = 0

        uniques = []
        index = []
        for end in range(len(fruits)):
            if fruits[end] not in uniques:
                uniques.append(fruits[end])
                index.append(end)
            else:
                index[uniques.index(fruits[end])] = end
            while len(uniques) > 2:
                start = min(index) + 1
                uniques.pop(index.index(min(index)))
                index.remove(min(index))


            maxSum = max(maxSum, (end - start + 1))

        return maxSum