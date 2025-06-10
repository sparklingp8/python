import random

data_list = [random.randrange(0, 10) for i in range(5)]
window_size = random.randrange(1, 3)
c_max = sum(data_list[:window_size])
nw_ttl = c_max
p1 = 0
ii = 0
jj = window_size - 1
for p2 in range(window_size, len(data_list)):
    nw_ttl = nw_ttl + data_list[p2]
    nw_ttl = nw_ttl - data_list[p1]
    if nw_ttl > c_max:
        c_max = nw_ttl
        ii = p1 + 1
        jj = p2
    p1 += 1
print(data_list, window_size)
print(c_max, ii, jj)
