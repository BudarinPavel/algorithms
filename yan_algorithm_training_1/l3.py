set_size = 10
my_set = [[] for _ in range(set_size)]


def add(x):
    if not find(x):
        my_set[x % set_size].append(x)
    return


def find(x):
    for now in my_set[x % set_size]:
        if now == x:
            return True
    return False


def delete(x):
    x_list = my_set[x % set_size]
    for i in range(len(x_list)):
        if x_list[i] == x:
            # x_list[i], x_list[len(x_list) - 1] = x_list[len(x_list) - 1], x_list[i]
            x_list[i] = x_list[len(x_list) - 1]
            x_list.pop()
            return


# A + B = X
def two_terms_with_sum_x(nums, x):
    prev_nums = set()
    for cur_num in nums:
        if x - cur_num in prev_nums:
            return cur_num, x - cur_num
        prev_nums.add(cur_num)
    return 0, 0


# Words with mistakes in dictionary
def words_in_dict(dictionary, text):
    all_words = set(dictionary)
    for word in dictionary:
        for mis_pos in range(len(word)):
            all_words.add(word[:mis_pos] + word[mis_pos + 1:])
    ans = []
    for word in text:
        ans.append(word in all_words)
    return ans

