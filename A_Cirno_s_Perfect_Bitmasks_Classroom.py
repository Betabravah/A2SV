t = int(input())

for _ in range(t):
    x = int(input())
    y = 0
    
    if x == 1:
        y = 3

    elif x & (x - 1) == 0:
        y = x + 1

    else:
        y = (x & (-x))
     
    print(y)
