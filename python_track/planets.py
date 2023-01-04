from collections import Counter
tests = int(input())

for test in range(tests):
    planets, cost = list(map(int, input().split()))
    orbits = list(map(int, input().split()))
    same_orbit = Counter(orbits)

    min_cost = 0
    for key in same_orbit:
        if same_orbit[key] == 1:
            min_cost += 1
        else:
            if cost > same_orbit[key]:
                min_cost += same_orbit[key]
            else:
                min_cost += cost

    print(min_cost)
