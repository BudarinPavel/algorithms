def solve_equation(a, b, c):
    ans = 'NO SOLUTION'

    if c < 0:
        ans = 'NO SOLUTION'
    elif a == 0 and c * c == b:
        ans = 'MANY SOLUTIONS'
    else:
        pot_ans = (c * c - b) / a
        if pot_ans - int(pot_ans) == 0:
            ans = int(pot_ans)
        else:
            ans = 'NO SOLUTION'

    return ans


a = int(input())
b = int(input())
c = int(input())

print(solve_equation(a, b, c))

# Tests:
# 0 9 3 -> MANY SOLUTIONS
# 2 2 3 -> NO SOLUTION
