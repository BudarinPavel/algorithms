def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l


# task about parents in school Board of Directors
def check_endowment(m, params):
    n, k = params
    return (k + m) * 3 >= n + m


# amount of solved leetcode exercises
def check_problem_count(days, params):
    n, k = params
    return (k + (k + days - 1)) * days


# task about stickers
def check_size(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n


def check_is_ge(index, params):
    seq, x = params
    return seq[index] >= x


def find_first_ge(seq, x):
    ans = l_bin_search(0, len(seq) - 1, check_is_ge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


# count x in sorted seq
def check_is_gt(index, params):
    seq, x = params
    return seq[index] > x


def check_is_ge(index, params):
    seq, x = params
    return seq[index] >= x


def find_first(seq, x, check):
    ans = l_bin_search(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans


def count_x(seq, x):
    index_gt = find_first(seq, x, check_is_gt)
    index_ge = find_first(seq, x, check_is_ge)
    return index_gt - index_ge


# mortgage percent
def check_monthly_perc(m_perc, y_perc):
    m_mult = 1 + m_perc / 100
    y_mult = 1 + y_perc / 100
    return m_mult**12 >= y_mult


def f_bin_search(l, r, eps, check, check_params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, check_params):
            r = m
        else:
            l = m
    return l


x = 12
eps = 0.0001
m_perc = f_bin_search(0, x, eps, check_monthly_perc, x)


# mortgage monthly payout
def check_credit(m_pay, params):
    periods, credit_sum, m_perc = params
    for i in range(periods):
        perc_pay = credit_sum * (m_perc / 100)
        credit_sum -= m_pay - perc_pay
    return credit_sum <= 0


def f_bin_search(l, r, eps, check, check_params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, check_params):
            r = m
        else:
            l = m
    return l


eps = 0.01
m = 10_000_000
n = 300
monthly_pay = f_bin_search(0, m, eps, check_credit, (n, m, m_perc))
print(monthly_pay)


# cyclist
def dist(t, params):
    x, v = params
    nim_pos = max_pos = x[0] + v[0] * t
    for i in range(1, len(x)):
        now_pos = x[i] + v[i] * t
        min_pos = min(min_pos, now_pos)
        max_pos = max(max_pos, now_pos)
    return max_pos - min_pos


def check_asc(t, eps, params):
    return dist(t + eps, params) >= dist(t, params)


def f_bin_search(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, eps, params):
            r = m
        else:
            l = m
    return l
