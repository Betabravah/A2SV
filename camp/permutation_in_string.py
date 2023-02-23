class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for right in range(len(s1)):
            count1[s1[right]] += 1
            count2[s2[right]] += 1

        if count1 == count2:
            return True

        left = 0
        right += 1
        while right < len(s2):
            if count1 == count2:
                return True
            count2[s2[left]] -= 1
            count2[s2[right]] += 1

            if count2[s2[left]] == 0:
                count2.pop(s2[left])
            left += 1
            right += 1
        if count1 == count2:
            return True
        return False



        #========================
        # count1 = Counter(s1)
        # d = len(s1)
        # for right in range(len(s1)):
        #     if count1[s2[right]] > 0:
        #         d -= 1
        # if d == 0:
        #     return True
        # left = 0
        # # right += 1
        # while right < len(s2):
        #     l = count1.get(s2[left], None)
        #     r = count1.get(s2[right], None)
        #     if r:
        #         count1[s2[right]] -= 1
        #         d -= 1
        #     if l:
        #         d += 1
        #     print(left, right, d)
        #     if d == 0:
        #         return True
        #     right += 1
        #     left += 1

        # return False

