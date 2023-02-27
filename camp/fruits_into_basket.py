class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = maxLen = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                left += 1
                
            maxLen = max(maxLen, right - left + 1)
        return maxLen


        
