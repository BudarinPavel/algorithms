def count_details(alloy_mass, billet_mass, workpiece_mass):
    if alloy_mass < billet_mass or billet_mass < workpiece_mass:
        return 0
    else:
        billet_cnt = alloy_mass // billet_mass
        workpieces_cnt = billet_cnt * (billet_mass // workpiece_mass)
        remain_alloy = alloy_mass % billet_mass + billet_cnt * (billet_mass % workpiece_mass)
        return workpieces_cnt + count_details(remain_alloy, billet_mass, workpiece_mass)


n, k, m = list(map(int, input().split()))
print(count_details(n, k, m))

# Test 1: 1 1 1 -> 1
# Test 2: 200 200 200 -> 1
# Test 3: 100 200 200 -> 0
# Test 4: 100 100 200 -> 0

# Test 5 is failed 31 9 4 -> 6

