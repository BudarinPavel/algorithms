n = int(input())
lang_all_know = set()
lang_smb_know = set()
for i in range(n):
    lang_amount = int(input())
    stud_langs = set()
    for j in range(lang_amount):
        stud_langs.add(input())
    if i == 0:
        lang_all_know = stud_langs
    lang_all_know = lang_all_know & stud_langs
    lang_smb_know = lang_smb_know | stud_langs

print(len(lang_all_know))
for lang in lang_all_know:
    print(lang)
print(len(lang_smb_know))
for lang in lang_smb_know:
    print(lang)
