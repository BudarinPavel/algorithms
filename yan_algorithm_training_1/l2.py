def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


def find_right_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans


def find_max(seq):
    ans = seq[0]
    for i in range(len(seq)):
        if seq[i] > ans:
            ans = seq[i]
        return ans


def find_max_2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif max2 < seq[i]:
            max2 = seq[i]
    return max1, max2


def short_words(words):
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    ans = []
    for word in words:
        if len(word) == min_len:
            ans.append(word)
    return ' '.join(ans)


def isle_flood(h):
    max_pos = 0
    for i in range(len(h)):
        if h[i] > max_pos:
            max_pos = i
    ans = 0
    cur_max = 0
    for i in range(max_pos):
        if h[i] > cur_max:
            cur_max = h[i]
        ans += cur_max - h[i]
    cur_max = 0
    for i in range(len(h) - 1, max_pos, -1):
        if h[i] > cur_max:
            cur_max = h[i]
        ans += cur_max - h[i]
    return ans


def rle(s):
    def pack(sym, cnt):
        if cnt > 1:
            return sym + str(cnt)
        return sym

    last_sym = s[0]
    last_pos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != last_sym:
            ans.append(pack(last_sym, i - last_pos))
            last_pos = i
            last_sym = s[i]
    ans.append(pack(s[last_pos], len(s) - last_pos))
    return ''.join(ans)


def find_min_even(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]
        return ans


# seq = list(map(float, input('Input sequence:').split()))
# x = float(input())

print(rle(input()))


'''
StakOverFlow:
from timeit import default_timer as timer
from datetime import timedelta

start = timer()

# ....
# (your code runs here)
# ...

end = timer()
print(timedelta(seconds=end-start))
'''
'''
YouTube comments:
ans_1 = short_words_1(some_words)
ans_1_time = timeit.timeit(lambda: short_words_1(some_words), number=10000000)
'''
