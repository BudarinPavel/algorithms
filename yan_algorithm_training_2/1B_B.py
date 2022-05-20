n, i, j = list(map(int, input().split()))


print(min(abs(i - j) - 1, min(i, j) + (n - max(i, j) - 1)))


