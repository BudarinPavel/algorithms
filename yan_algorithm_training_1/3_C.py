n, m = list(map(int, input().split()))
annyas_cubs = set(int(input()) for i in range(n))
boryas_cubs = set([int(input()) for i in range(m)])

both_cubs = annyas_cubs & boryas_cubs
print(len(both_cubs))
print(*sorted(both_cubs))
print(len(annyas_cubs - both_cubs))
print(*sorted(annyas_cubs - both_cubs))
print(len(boryas_cubs - both_cubs))
print(*sorted(boryas_cubs - both_cubs))

