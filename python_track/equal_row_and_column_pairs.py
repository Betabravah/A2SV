class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        for rowIdx, row in enumerate(grid):
            rows[rowIdx] = row
            for colIdx, col in enumerate(row):
                cols[colIdx].append(col)

        ctr = 0
        for row in rows.values():
            count = 0
            for col in cols.values():
                if col == row:
                    count += 1
            ctr += count

        return ctr
