def get_playground(rows, cols, coords):
    def count_mines_around(x, y, coords):
        mines_cnt = 0
        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if row in coords and col in coords[row]:
                    mines_cnt += 1
        return mines_cnt

    for i in range(rows):
        for j in range(cols):
            if i in coords and j in coords[i]:
                print('*', end='')
                if j != cols - 1:
                    print(' ', end='')
            else:
                print(str(count_mines_around(i, j, coords)), end='')
                if j != cols - 1:
                    print(' ', end='')
        if i != rows - 1:
            print()


n, m, k = list(map(int, input().split()))
coords = {}
for i in range(k):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    if x not in coords:
        coords[x] = []
    coords[x].append(y)

get_playground(n, m, coords)

