def make_symmetric(seq):
    def is_symmetric(seq):
        center = len(seq) // 2
        if len(seq) % 2 == 0:
            return seq[:center] == seq[center:][::-1]
        else:
            return seq[:center] == seq[center + 1:][::-1]

    m = 0
    addition = []
    new_seq = seq.copy()
    center = len(seq) // 2
    while not is_symmetric(new_seq):
        if seq[center - 1] == seq[center]:
            right = seq[center + 1:][::-1]
            left = seq[center - 1 - len(right):center - 1]

            if right == left:
                addition = seq[:center -1 - len(right)][::-1]
                m = len(addition)
                new_seq += addition
            else:
                center += 1


        else:
            right = seq[center + 1:][::-1]
            left = seq[center - len(right):center]

            if right == left:
                addition = seq[:center - len(right)][::-1]
                m = len(addition)
                new_seq += addition
            else:
                center += 1
    return m, addition


n = int(input())
seq = list(map(int, input().split()))
m, addition = make_symmetric(seq)
print(m, end='')
if m != 0:
    print()
    print(*addition, end='')

