x = int(input())
m = x
cnt = 1

while x != 0:
    x = int(input())
    if x > m:
        m = x
        cnt = 1
    elif x == m:
        cnt += 1

print(cnt)

