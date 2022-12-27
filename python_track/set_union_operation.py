# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = input().split(' ')
b = int(input())
french = input().split(' ')

total = set(english + french)
print(len(total))
