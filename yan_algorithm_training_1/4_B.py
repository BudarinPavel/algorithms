dict = {}
with open('input_4B.txt') as f:
    text = f.read().split()
    for w in text:
        if w not in dict:
            dict[w] = 0
        else:
            dict[w] += 1
        print(dict[w], end=' ')

