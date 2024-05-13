## RIGHT SHIFT ##
a = [1, 2, 3, 4, 5]
k = 3
l: int = len(a)
k = k % l
for _ in range(k):
    t = a[-1]
    for i in range(l - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = t

print(a)

## LEFT SHIFT ##
a = [1, 2, 3, 4, 5]
k = 5
l: int = len(a)
k = k % l
for _ in range(k):
    t = a[0]
    for i in range(0, l-1):
        a[i] = a[i + 1]
    a[l-1] = t

print(a)