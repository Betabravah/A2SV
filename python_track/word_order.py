# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
_dict = {}

for _ in range(n):
    x = input()
    _dict[x] = 1 + _dict.get(x, 0)
    
print(len(_dict))
for i in _dict.values():
    print(i, end=" ")
        
