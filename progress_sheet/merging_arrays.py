n, m = list(map(int, input().split()))
p1 = p2 = 0
 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
sorted = []
while p1 < n and p2 < m:
        if arr1[p1] < arr2[p2]:
            sorted.append(arr1[p1])
            p1 += 1
        else:
            sorted.append(arr2[p2])
            p2 += 1
 
sorted.extend(arr2[p2:])
sorted.extend(arr1[p1:])
   
 
print(*sorted)
