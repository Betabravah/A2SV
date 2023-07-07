from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    # Write your code here.
        graph = [[] for _ in range(n+1)]
        count = [0 for _ in range(n+1)]

        for a, b in prerequisites:
            graph[a].append(b)
            count[b] += 1


        queue = deque()
        visited = set()
        for i in range(1, n + 1):
            if count[i] == 0:
                queue.append(i)
                visited.add(i)

        ctr = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                cur = queue.popleft()

                for child in graph[cur]:
                    count[child] -= 1

                    if count[child] == 0:
                        queue.append(child)
                        visited.add(child)
            ctr += 1


        if len(visited) != n:
            return -1

        return ctr



