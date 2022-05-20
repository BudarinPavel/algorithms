s = input()
cnt = 0

if len(s) == 1:
    print(0)
else:
    if len(s) % 2 == 0:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2:][::-1]
    else:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2 + 1:][::-1]

    for i in range(len(s) // 2):
        if s1[i] != s2[i]:
            cnt += 1
    print(cnt)

