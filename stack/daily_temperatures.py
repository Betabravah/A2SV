class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            else:
                stack.append([temperatures[i], i]) # append value with its index

        return answer
