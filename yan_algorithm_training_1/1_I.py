def max2(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


def can_through_away(sizes):
    a, b, c, d, e = sizes
    hole_width, hole_high = max(a, e), min(d, e)
    brick_width, brick_height = max2(a, b, c), min(a, b, c)

    return 'YES' if brick_width <= hole_width and brick_height <= hole_high else 'NO'


sizes = []
for i in range(5):
    sizes.append(int(input()))

print(can_through_away(sizes))

# Extra test:
# 1:
# 2:
# 3:


