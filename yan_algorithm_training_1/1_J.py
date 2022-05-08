def solve_lin_system(coefs):
    a, b, c, d, e, f = coefs
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
        return str(5)
    elif a == 0 and c == 0 and b != 0 and d != 0 and e / b == f / d:
        return '4 ' + str(e / b)
    elif a != 0 and c != 0 and b == 0 and d == 0 and e / a == f / c:
        return '3 ' + str(e / a)
    elif a * d != b * c:
        x_0 = (d * e - b * f) / (a * d - b * c)
        y_0 = (a * f - c * e) / (a * d - b * c)
        return '2 ' + str(x_0) + ' ' + str(y_0)
    elif b != 0 and d != 0 and e / b == f / d and a // b == c / d:
        return '1 ' + str(-a / b) + ' ' + str(e / b)
    else:
        return '0'


coefs = tuple(float(input()) for i in range(6))
print(solve_lin_system(coefs))

