## RIGHT SHIFT ##
a = [1, 2, 3, 4, 5]
k = 2 
l: int = len(a)
k = k % l
a = a[::-1]  #reverse array
a = a[:k][::-1] + a[k::][::-1]  #reverse first k elements

print(a)

## LEFT SHIFT ##
a = [1, 2, 3, 4, 5]
k = 3
l: int = len(a)
k = k % l
a = a[::-1]  #reverse array
a =  a[:l-k][::-1] + a[l-k:][::-1] #reverse first l-k elements

print(a)
