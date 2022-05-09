def find_third_max(l):
    if l[0] >= l[1] and l[0] >= l[2]:
        max1 = l[0]
        max2, max3 = (l[1], l[2]) if l[1] >= l[2] else (l[2], l[1])
    elif l[1] >= l[2] and l[1] >= l[0]:
        max1 = l[1]
        max2, max3 = (l[0], l[2]) if l[0] >= l[2] else (l[2], l[0])
    else:
        max1 = l[2]
        max2, max3 = (l[1], l[0]) if l[1] >= l[0] else (l[0], l[1])
    for num in l[3:]:
        if num >= max1:
            max3, max2, max1 = max2, max1, num
        elif num >= max2:
            max3, max2 = max2, num
        elif num > max3:
            max3 = num
    return max3





def find_vasya_position(distances):
    def potential_vasya(distances, winner_result):
        is_winner_before = distances[0] == winner_result
        best_pos = 0
        for i in range(1, len(distances) - 1):
            if (is_winner_before and
                    distances[i] % 10 == 5 and
                    distances[i + 1] < distances[i]):
                if best_pos == 0:
                    best_pos = i
                elif distances[i] > distances[best_pos]:
                    best_pos = i
            elif distances[i] == winner_result:
                is_winner_before = True
        return best_pos

    # find winner result O(n)
    winner_result = max(distances)

    # find potential Vasay position O(n)
    potential_pos = potential_vasya(distances, winner_result)

    # upgrade Vasya pos
    if potential_pos == 0:
        return 0
    else:
        betters = 0
        unique = []
        for dist in distances:
            if dist > distances[potential_pos]:
                if dist not in unique:
                    unique.append(dist)
                else:
                    betters += 1
        return len(unique) + betters + 1


n = int(input())
distances = list(map(int, input().split()))

print(find_vasya_position(distances), end='')

