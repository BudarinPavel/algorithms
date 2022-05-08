def get_min_max_platform_time(first_int, second_int, first_amount, second_amount):
    min_first_time = first_amount * 1 + (first_amount - 1) * first_int
    min_second_time = second_amount * 1 + (second_amount - 1) * second_int
    max_first_time = min_first_time + 2 * first_int
    max_second_time = min_second_time + 2 * second_int
    if max_first_time < min_second_time or max_second_time < min_first_time:
        return str(-1)
    else:
        return str(max(min_first_time, min_second_time)) + ' ' + str(min(max_first_time, max_second_time))


a = int(input())
b = int(input())
n = int(input())
m = int(input())

print(get_min_max_platform_time(a, b, n, m))

