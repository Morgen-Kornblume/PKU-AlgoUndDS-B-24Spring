a = b = []
b.append(1)
print(a)  		#>>[1]
a = [[0]] * 3 #a中的3个元素都指向同一张列表[0]
a[0].append(1)
print(a)  #>>[[0, 1], [0, 1], [0, 1]]
print(b)