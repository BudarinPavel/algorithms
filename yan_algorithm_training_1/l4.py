def count_sort(seq):
    min_val = min(seq)
    max_val = max(seq)
    k = max_val - min_val + 1
    count = [0] * k
    for now in seq:
        count[now - min_val] += 1
    cur_pos = 0
    for val in range(k):
        for i in range(count[val]):
            seq[cur_pos] = val + min_val
            cur_pos += 1


def is_digit_permutation(x, y):
    def count_digits(num):
        digits_count = [0] * 10
        while num != 0:
            digits_count[num % 10] += 1
            num //= 10
        return digits_count

    digits_x = count_digits(x)
    digits_y = count_digits(y)
    for i in range(10):
        if digits_x[i] != digits_y[i]:
            return False
    return True


def count_beating_rooks(rook_coords):
    def add_rook(key, row_o_col):
        if key not in row_o_col:
            row_o_col[key] = 0
        row_o_col[key] += 1

    def count_pairs(row_o_col):
        pairs = 0
        for key in row_o_col:
            pairs += row_o_col[key]
        return pairs

    rooks_in_row = {}
    rooks_in_col = {}
    for row, col in rook_coords:
        add_rook(row, rooks_in_row)
        add_rook(col, rooks_in_col)
    return count_pairs(rooks_in_row) + count_pairs(rooks_in_col)


def string_hist(s):
    sym_count = {}
    max_sym_cnt = 0
    for sym in s:
        if sym not in sym_count:
            sym_count[sym] = 0
        sym_count[sym] += 1
        max_sym_cnt = max(max_sym_cnt, sym_count[sym])
    sorted_uniq_syms = sorted(sym_count.keys())
    for row in range(max_sym_cnt, 0, -1):
        for sym in sorted_uniq_syms:
            if sym_count[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_uniq_syms))


def group_key(words):
    def key_by_word(word):
        return ''.join(sorted(word))

    groups = {}
    for word in words:
        group_key = key_by_word(word)
        if group_key not in groups:
            groups[group_key] = 0
        groups[group_key].append(word)
    ans = []
    for group_key in groups:
        ans.append(groups[group_key])
    return ans





