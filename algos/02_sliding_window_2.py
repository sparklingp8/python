import random

data_list = "bacacbefaobeacfe"  # [chr(random.randrange(97, 123)) for i in range(10)]
window_size = 5  # random.randrange(3, 5)
c_max = len([c for c in data_list[:window_size] if c in ['a', 'e', 'i', 'o', 'u']])
nw_ttl = c_max
p1 = 0
ii = 0
jj = window_size - 1
for p1 in range(len(data_list) - window_size):
    if data_list[p1 + window_size] in ['a', 'e', 'i', 'o', 'u']:
        nw_ttl += 1
    if data_list[p1] in ['a', 'e', 'i', 'o', 'u']:
        nw_ttl -= 1
    if nw_ttl > c_max:
        c_max = nw_ttl
        ii = p1 + 1
        jj = p1 + window_size

print(data_list, window_size)
print(c_max, ii, jj)
