a = [1,2,3,4]
b = [1,2,3,4]
print( a == b) #>>True
print( a is b) #>>False
c = a
print( a == c) #>>True
print( a is c) #>>True
a[0] = 5
print( a == c) #>>True
print( a is c) #>>True
print(c)