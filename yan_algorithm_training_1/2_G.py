def max_two_production(l):
    if len(l) == 2:
        return (l[0], l[1]) if l[0] < l[1] else (l[1], l[0])
    else:
        maxs, mins = [0, 0], [0, 0]
        for cur in l:
            if cur > maxs[1]:
                maxs[0] = maxs[1]
                maxs[1] = cur
            elif maxs[0] < cur <= maxs[1]:
                maxs[0] = cur
            elif cur < mins[0]:
                mins[1] = mins[0]
                mins[0] = cur
            elif mins[0] < cur < mins[1]:
                mins[1] = cur
        return maxs if maxs[0] * maxs[1] > mins[0] * mins[1] else mins


numbers = list(map(int, input().split()))

print(*max_two_production(numbers), end='')

