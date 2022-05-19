from timeit import default_timer as timer
from datetime import timedelta

start = timer()

# def get_dots(coords, l):
#     next_pos = coords.copy()
#     for coord in coords:
#         for x in range(- l, l + 1):
#             for y in range(- l, l + 1):
#                 if abs(x) + abs(y) <= l:
#                     next_pos.add((coord[0] + x, coord[1] + y))
#     return next_pos


# def able_to_run(coords, nav, l):
#     intercect = set()
#     for point in coords:
#         for xy in nav:
#             if abs(point[0] - xy[0]) + abs(point[1] - xy[1]) <= l:
#                 intercect.add((xy[0], xy[1]))
#     return intercect


t, d, n = list(map(int, input().split()))
possible_pos = set()
possible_pos.add((0, 0))
for i in range(n):
    nav_xy = set()
    nav_xy.add(tuple(map(int, input().split())))

    # navigator = get_dots(nav_xy, d)
    navigator = nav_xy.copy()
    for coord in nav_xy:
        for x in range(-d, d + 1):
            for y in range(-d, d + 1):
                if abs(x) + abs(y) <= d:
                    navigator.add((coord[0] + x, coord[1] + y))

    # possible_pos = able_to_run(possible_pos, navigator, t)
    possible_pos_temp = set()
    for point in possible_pos:
        for xy in navigator:
            if abs(point[0] - xy[0]) + abs(point[1] - xy[1]) <= t:
                possible_pos_temp.add((xy[0], xy[1]))
    possible_pos = possible_pos_temp

print(len(possible_pos))
for coord in possible_pos:
    print(*coord)

end = timer()
print(timedelta(seconds=end-start))
