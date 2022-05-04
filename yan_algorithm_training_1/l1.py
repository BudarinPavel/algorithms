import math


def frequent_sym(s):
    ans = ''
    ans_cnt = 0
    sym_cnt = {}
    for now in sym_cnt:
        if now not in sym_cnt:
            sym_cnt[now] = 0
        sym_cnt[now] += 1
        if sym_cnt[now] > ans_cnt:
            ans = now
            ans_cnt = sym_cnt[now]
    return ans


def square_equation(a, b, c):
    ans = 'No solution'
    if a == 0:
        if b != 0:
            print(-c / b)
        elif c == 0:
            ans = 'Infinite number of solutions'
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x1 = -b / (2 * c)
            ans = x1
        elif d > 0:
            x1 = (-b - math.sqrt(d)) / (2 * a)
            x2 = (-b + math.sqrt(d)) / (2 * a)
            if x1 < x2:
                ans = x1, x2
            else:
                ans = x2, x1
    return ans


s = input()

print(frequent_sym(s))

