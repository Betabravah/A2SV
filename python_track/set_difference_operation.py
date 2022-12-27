# Enter your code here. Read input from STDIN. Print output to STDOUT
english_numbers = int(input())
english_subscribers = input().split(' ')
french_numbers = int(input())
french_subscribers = input().split(' ')

ctr = 0
for student in english_subscribers:
    if student not in french_subscribers:
        ctr += 1
print(ctr)
