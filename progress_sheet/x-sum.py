tests = int(input())
for test in range(tests):
    matrix = []
    rows, cols = list(map(int, input().split()))
    for r in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    maximum = 0
    diagonal = {}       
    rdiagonal = {}
    for row in range(rows):
        for col in range(cols):
            sums = row + col
            if sums in rdiagonal:
                rdiagonal[sums] += matrix[row][col]
            else:
                rdiagonal[sums] = matrix[row][col]
            diff = col - row
            if diff in diagonal:
                diagonal[diff] += matrix[row][col]
            else:
                diagonal[diff] = matrix[row][col]
    for row in range(rows):
        for col in range(cols):
            sums = row + col
            diff = col - row
            all_sum = rdiagonal[sums] + diagonal[diff] - matrix[row][col]
            maximum = max(maximum, all_sum)
    
    print(maximum)
