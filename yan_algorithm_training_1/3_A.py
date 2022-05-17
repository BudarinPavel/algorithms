from timeit import default_timer as timer
from datetime import timedelta

start = timer()

s = input() + ' '
met = set()
i = 0
while i < len(s):
    s_num = s[i:s.find(' ', i)]
    met.add(s_num)
    i = s.find(' ', i) + 1

print(len(met))

end = timer()
print(timedelta(seconds=end-start))
