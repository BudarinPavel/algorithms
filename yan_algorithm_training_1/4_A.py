n = int(input())
syn_dict = {}
for i in range(n):
    word, synonym = input().split()
    syn_dict[word] = synonym
word = input()
if word in syn_dict:
    print(syn_dict[word])
else:
    for w, syn in syn_dict.items():
        if word == syn:
            print(w)
