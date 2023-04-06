from collections import defaultdict

nodes = int(input())
k = int(input())

graph = defaultdict(list)

for _ in range(k):
    op = list(map(int, input().split()))

    if op[0] == 1:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])

    elif op[0] == 2 and graph[op[1]]:
        print(*graph[op[1]])
