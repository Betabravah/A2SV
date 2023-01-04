class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        oneRows = defaultdict(int)
        oneCols = defaultdict(int)
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == 1:
                    oneRows[row_index] += 1
                    oneCols[col_index] += 1


        rows, cols = row_index+1, col_index+1
        difference_matrix = []
        for row_index, row in enumerate(grid):
            row_ones = oneRows[row_index]
            row_zeroes = cols - row_ones

            
            diff_row = []
            for col_index, col in enumerate(row):
                diff = 0
                col_ones = oneCols[col_index]
                col_zeroes = rows - col_ones

                diff += (row_ones + col_ones - row_zeroes - col_zeroes )
                diff_row.append(diff)

            difference_matrix.append(diff_row)

        return difference_matrix
