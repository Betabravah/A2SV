# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split(' '))
sets = int(input())


for i in range(sets):
    b = set(input().split(' '))
    if len(a) > len(b):
        if not b.issubset(a):
            print('False')
            break
else:
    print('True')
