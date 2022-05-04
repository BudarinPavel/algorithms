k1, m, k2, p2, n2 = list(map(int, input().split()))

if n2 != 1:
    min_flats = (k2 - 1) // n2 + 1
    max_flats = k2 // (n2 - 1)
    if min_flats == max_flats:
        flats_on_floor = min_flats
        flats_in_p = m * flats_on_floor
        p1 = (k1 - 1) // flats_in_p + 1
        n1 = ((k1 % flats_in_p) - 1) // flats_on_floor + 1

print(p1, n1)


