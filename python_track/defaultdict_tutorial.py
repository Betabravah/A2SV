# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split(' '))

d = defaultdict(list)
for i in range(1, n+1):
    d[input()].append(i)
for i in range(m):
    b_element = input()
    if b_element in d:
        lst = map(str, d[b_element])
        print(' '.join(lst))
    else:
        print(-1)
