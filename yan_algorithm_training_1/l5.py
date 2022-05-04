# range sum quire
def make_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums + 1)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum


def rsq(prefix_sum, l, r):
    return prefix_sum[r] - prefix_sum[l]


# range len is N and M quires to that range like "How many zeros in subrange"
def make_prefix_zeros(nums):
    prefix_zeros = [0] * (len(nums) + 1)
    for i in range(1, len(nums + 1)):
        if nums[i - 1] == 0:
            prefix_zeros[i] = prefix_zeros[i - 1] + 1
        else:
            prefix_zeros[i] = prefix_zeros[i - 1]
    return prefix_zeros


def count_zeros(prefix_zeros, l, r):
    return prefix_zeros[r] - prefix_zeros[l]


# find all sub-ranges with zero-sum in range N
# O(N^3)
def count_zeros_sum_ranges(nums):
    cnt_ranges = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            range_sum = 0
            for k in range(i, j):
                range_sum += nums[k]
            if range_sum == 0:
                cnt_ranges += 1
    return cnt_ranges


# O(N^2)
def count_zeros_sum_ranges(nums):
    cnt_ranges = 0
    for i in range(len(nums)):
        range_sum = 0
        for j in range(i, len(nums)):
            range_sum += nums[j]
            if range_sum == 0:
                cnt_ranges += 1
    return cnt_ranges


# O(N)
def count_prefix_sums(nums):
    prefix_sum_by_value = {0: 1}
    now_sum = 0
    for now in nums:
        now_sum += now
        if now_sum not in prefix_sum_by_value:
            prefix_sum_by_value[now_sum] = 0
        prefix_sum_by_value[now_sum] += 1
    return prefix_sum_by_value


def count_zeros_sum_ranges(prefix_sum_by_value):
    cnt_ranges = 0
    for now_sum in prefix_sum_by_value:
        cnt_sum = prefix_sum_by_value[now_sum]
        cnt_ranges += cnt_sum * (cnt_sum - 1) // 2
    return cnt_ranges


def count_pairs_with_diff_gtk(sorted_nums, k):
    cnt_pairs = 0
    last = 0
    for first in range(len(sorted_nums)):
        while last < len(sorted_nums) and sorted_nums[last] - sorted_nums[first] <= k:
            last += 1
        cnt_pairs += len(sorted_nums) - last
    return cnt_pairs


def best_team_sum(players):
    best_sum = 0
    now_sum = 0
    last = 0
    for first in range(len(players)):
        while last < len(players) and (last == first or players[first] + players[first + 1] >= players[last]):
            now_sum += players[last]
            last += 1
        best_sum = max(best_sum, now_sum)
        now_sum -= players[first]
    return best_sum


def merge(nums_1, nums_2):
    merged = [0] * (len(nums_1) + len(nums_2))
    p_1 = p_2 = 0
    for k in range(len(nums_1) + len(nums_2)):
        if p_1 != len(nums_1) and (p_2 == len(nums_2) or nums_1[p_1] < nums_2[p_2]):
            merged[k] = nums_1[p_1]
            p_1 += 1
        else:
            merged[k] = nums_2[p_2]
            p_2 += 1
    return merged

