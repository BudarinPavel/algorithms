from timeit import default_timer as timer
from datetime import timedelta

start = timer()

# ....
# (your code runs here)
# ...




# def is_boudary(point, coords):
#     boundary_points = set()
#     boundary_points.add((point[0] - 1, point[1]))
#     boundary_points.add((point[0] + 1, point[1]))
#     boundary_points.add((point[0], point[1] - 1))
#     boundary_points.add((point[0], point[1] + 1))
#     for point in boundary_points:
#         if point not in coords:
#             return True
#     return False

def get_dots(coords, l):
    next_pos = coords.copy()
    for coord in coords:
        for x in range(- l, l + 1):
            for y in range(- l, l + 1):
                if (abs(x) + abs(y) <= l and
                    ((coord[0] - 1, coord[1]) not in coords or
                     (coord[0] + 1, coord[1]) not in coords or
                     (coord[0], coord[1] - 1) not in coords or
                     (coord[0], coord[1] + 1) not in coords)): # and is_boudary((coord[0] + x, coord[1] + y), coords):
                    next_pos.add((coord[0] + x, coord[1] + y))
    return next_pos


t, d, n = list(map(int, input().split()))
possible_pos = set()
possible_pos.add((0, 0))
for i in range(n):
    possible_pos = get_dots(possible_pos, t)
    nav_xy = set()
    nav_xy.add(tuple(map(int, input().split())))
    navigator = get_dots(nav_xy, d)
    possible_pos = possible_pos & navigator

print(len(possible_pos))
for coord in possible_pos:
    print(*coord)

end = timer()
print(timedelta(seconds=end-start))
