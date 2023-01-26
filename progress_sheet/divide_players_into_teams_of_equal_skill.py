class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team = skill[0] + skill[-1]
        left, right = 1, len(skill)-2
        chemSum = skill[0] * skill[-1]
        while left < right:
            newTeam = skill[left] + skill[right]
            if newTeam != team:
                return -1
            newChem = skill[left] * skill[right]
            chemSum += newChem
            left += 1
            right -= 1
        return chemSum
