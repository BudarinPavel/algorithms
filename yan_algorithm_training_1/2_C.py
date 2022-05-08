def closest_number_to_x(nums, x):
    ans_index = 0
    min_dist = abs(x - nums[ans_index])
    for i in range(1, len(nums)):
        if abs(x - nums[i]) < min_dist:
            min_dist = abs(x - nums[i])
            ans_index = i
    return nums[ans_index]


n = int(input())
nums = list(map(int, input().split()))
x = int(input())

print(closest_number_to_x(nums, x))

