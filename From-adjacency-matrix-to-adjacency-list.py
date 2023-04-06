nodes = int(input())

mat = []
for _ in range(nodes):
    row = list(map(int, input().split()))

    mat.append(row)


for ridx, row in enumerate(mat):
    edges = []
    for cidx, col in enumerate(row):
        if col:
            edges.append(cidx+1)

    print(len(edges), *edges)
