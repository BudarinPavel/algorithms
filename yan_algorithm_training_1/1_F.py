def find_best_placement(sizes):
    a, b, c, d = sizes
    h1, w1, h2, w2 = min(a, b), max(a, b), min(c, d), max(c, d)

    s1 = (w1 + w2) * max(h1, h2)
    s2 = max(w1, w2) * (h1 + h2)
    s3 = (w1 + h2) * max(w2, h1)
    s4 = (w2 + h1) * max(w1, h2)

    if s1 <= s2 and s1 <= s3 and s1 <= s4:
        return w1 + w2, max(h1, h2)
    elif s2 <= s1 and s2 <= s3 and s2 <= s4:
        return max(w1, w2), h1 + h2
    elif s3 <= s1 and s3 <= s2 and s3 <= s4:
        return w1 + h2, max(w2, h1)
    return w2 + h1, max(w1, h2)


laptops_sizes = list(map(int, input().split()))
ans = tuple(map(str, find_best_placement(laptops_sizes)))
print(' '.join(ans))

# Extra test:
# 1: 5 5 3 3 -> 8 5
# 2: 1 1 1 1 -> 2 1
# 3: 1000 999 1000 999 -> 2000 999


