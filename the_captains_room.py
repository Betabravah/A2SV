# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
lst = sorted([int(x) for x in input().split()])

i = 0
while i < len(lst):
    try:
        if lst[i] != lst[i+1]:
            print(lst[i])
            break
    except:
        print(lst[-1])
    i += k

