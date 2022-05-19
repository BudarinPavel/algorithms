n = int(input())
turtels = set()
for i in range(n):
    a, b = list(map(int, input().split()))
    if a + b == n - 1 and a >= 0 and b >= 0:
        turtels.add(a+1)
print(len(turtels), end='')


