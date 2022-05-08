STOP = -2 * 10 ** 9


def is_constant(l):
    i = 1
    while i < len(l):
        if l[i - 1] != l[i]:
            return False
        i += 1
    return True


def is_ascending(l):
    i = 1
    while i < len(l) - 1:
        if not l[i - 1] < l[i]:
            return False
        i += 1
    return True


def is_weakly_ascending(l):
    i = 1
    while i < len(l):
        if not l[i - 1] <= l[i]:
            return False
        i += 1
    return True


def is_descending(l):
    i = 1
    while i < len(l):
        if not l[i - 1] > l[i]:
            return False
        i += 1
    return True


def is_weakly_descending(l):
    i = 1
    while i < len(l):
        if not l[i - 1] >= l[i]:
            return False
        i += 1
    return True


def type_of_seq(l):
    if not l:
        return 'RANDOM'
    elif is_constant(l):
        return 'CONSTANT'
    elif is_ascending(l):
        return 'ASCENDING'
    elif is_weakly_ascending(l):
        return 'WEAKLY ASCENDING'
    elif is_descending(l):
        return 'DESCENDING'
    elif is_weakly_descending(l):
        return 'WEAKLY DESCENDING'
    return 'RANDOM'


l = []
cur = float(input())
while cur != STOP:
    l.append(cur)
    cur = float(input())

print(type_of_seq(l))

