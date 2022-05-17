def clear(text):
    escape = '.,;:-!?'
    for c in escape:
        text = text.replace(c, '')
    return text


with open('input.txt') as f:
    text = set(f.read().split())
print(len(text))

