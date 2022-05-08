def is_ascending(l):
    ans = True
    i = 1
    while i <= (len(l) - 1) and ans:
        if not l[i - 1] < l[i]:
            ans = False
        i += 1
    return 'YES' if ans else 'NO'


l = list(map(float, input().split()))

print(is_ascending(l))