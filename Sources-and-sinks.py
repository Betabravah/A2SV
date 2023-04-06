from collections import defaultdict
nodes = int(input())

mat = []
for _ in range(nodes):
    row = list(map(int, input().split()))

    mat.append(row)

cols = defaultdict(int)
rows = defaultdict(int)
for ridx, row in enumerate(mat):
    sources, sinks = [], []
    for cidx, col in enumerate(row):
        cols[cidx] += int(col)
        rows[ridx] += int(col)

sources = []
for key, value in cols.items():
    if value == 0:
        sources.append(key + 1)


sinks = []
for key, value in rows.items():
    if value == 0:
        sinks.append(key + 1)
            

print(len(sources), *sources)
print(len(sinks), *sinks)
