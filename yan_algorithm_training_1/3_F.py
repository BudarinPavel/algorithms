def calc_power_of_closeness(g1, g2):
    def get_base(g):
        base = {}
        for i in range(len(g) - 1):
            cur_base = g[i:i + 2]
            if cur_base not in base:
                base[cur_base] = 0
            base[cur_base] += 1
        return base

    base1 = get_base(g1)
    base2 = get_base(g2)

    closeness = 0
    for base in base1:
        if base in base2:
            # closeness += base1[base] * base2[base]
            closeness += base1[base]

    return closeness



genom1, genom2 = input(), input()
print(calc_power_of_closeness(genom1, genom2))

