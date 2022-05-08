def count_gt_neighbours(l):
    cnt = 0
    for i in range(1, len(l) - 1):
        if l[i - 1] < l[i] > l[i + 1]:
            cnt += 1
    return cnt


numbers = list(map(float, input().split()))

print(count_gt_neighbours(numbers))

