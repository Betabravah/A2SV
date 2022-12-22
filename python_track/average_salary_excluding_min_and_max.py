class Solution:
    def average(self, salary: List[int]) -> float:
        x = min(salary)
        y = max(salary)
        return (sum(salary)-(x+y))/(len(salary)-2)
