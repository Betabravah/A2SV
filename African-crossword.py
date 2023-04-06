from collections import defaultdict
n, m = map(int, input().split())

row_count = defaultdict(list)
col_count = defaultdict(list)

grid = []
for i in range(n):
    row = input()
    grid.append(row)
    for j, char in enumerate(row):
        row_count[i].append(char)
        col_count[j].append(char)


decrypted = []
for ridx, row in enumerate(grid):
    for cidx, col in enumerate(row):
        if row_count[ridx].count(col) == 1 and col_count[cidx].count(col) == 1:
            decrypted.append(col)


print(''.join(decrypted))

    
