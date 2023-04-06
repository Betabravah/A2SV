from collections import defaultdict

nodes = int(input())

graph = defaultdict(list)
count = 0
for i in range(nodes):
    row = list(map(int, input().split()))
    
    for j in range(i, len(row)):
        count += row[j]


print(count)
