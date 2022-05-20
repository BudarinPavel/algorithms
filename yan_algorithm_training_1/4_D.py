n = int(input())
keys_limits = {}
keys = list(map(int, input().split()))
for i in range(1, n + 1):
    keys_limits[i] = keys[i - 1]
k = int(input())
taps = list(map(int, input().split()))
key_taps = {}
for tap in taps:
    if tap not in key_taps:
        key_taps[tap] = 0
    key_taps[tap] += 1
for i in range(1, n + 1):
    if key_taps[i] > keys_limits[i]:
        print('YES')
    else:
        print('NO')



