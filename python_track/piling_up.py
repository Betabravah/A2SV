# Enter your code here. Read input from STDIN. Print output to STDOUT

def pilingUp(cube_number, cubes): 
    left = 0
    right = cube_number-1
    temp = float('inf')
    while left <= right:
        if cubes[left] >= cubes[right] :
            if cubes[left] > temp:
                return "No"
                break
            else:
                temp = cubes[left]
                left += 1
        elif cubes[right] > cubes[left]:
            if cubes[right] > temp:
                return "No"
                break
            else:
                temp = cubes[right]
                right -= 1
    else:
        return "Yes"
            
    
    

if __name__ == '__main__':
    tests = int(input())

    for test in range(tests):
        cube_number = int(input())
        cubes = list(map(int, input().split(' ')))
        print(pilingUp(cube_number, cubes))
    

