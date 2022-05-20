buildings = input().split()
m_len = 0
for i in range(1, 11):
    if buildings[i - 1] == '1':
        closest = 10
        for j in range(1, 11):
            if buildings[j - 1] == '2' and abs(j - i) < closest:
                closest = abs(j - i)
        if closest > m_len:
            m_len = closest
print(m_len)

