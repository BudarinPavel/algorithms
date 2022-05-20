n = int(input())
blocks = {}
for i in range(n):
    w, h = list(map(int, input().split()))
    if w not in blocks:
        blocks[w] = h
    elif h > blocks[w]:
        blocks[w] = h
print(sum(blocks.values()))

