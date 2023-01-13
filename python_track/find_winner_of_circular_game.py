class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1, n+1):
            queue.append(i)

        cur = 0
        while len(queue) > 1:
            idx = (cur + k-1) % n
            while cur != idx:
                queue.append(queue[0])
                queue.popleft()
                cur = (cur+1) % n
            queue.popleft()

        return queue[0]
