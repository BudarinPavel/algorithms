n = int(input())
x_coords = set()

for _ in range(n):
    x, y = list(map(int, input().split()))
    if x not in x_coords:
        x_coords.add(x)
print(len(x_coords))
