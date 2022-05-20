dict = {}
with open('input_4C.txt') as f:
    text = f.read().split()
    most = 0
    for w in text:
        if w not in dict:
            dict[w] = 0
        dict[w] += 1
        if dict[w] > most:
            most = dict[w]

print(min([k for k, v in dict.items() if v == most]), end='')



