n, m = list(map(int, input().split()))
p1 = p2 = 0
 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
indices = []
lessNums = 0
while p1 < n and p2 < m:
        if arr1[p1] < arr2[p2]:
            p1 += 1
            lessNums += 1
        else:
            indices.append(lessNums)
            p2 += 1
while p2 < m:
    indices.append(lessNums)
    p2 += 1
 
print(*indices)
