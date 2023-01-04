tests = int(input())
for test in range(tests):
    letters_count = int(input())
    numbers = input().split(' ')
    letters = input()

    _dict = {}
    for index, number in enumerate(numbers):
        letter = _dict.get(number, None)
        if not letter:
            _dict[number] = letters[index]
        elif letter != letters[index]:
            print('NO')
            break
    else:
        print('YES')
