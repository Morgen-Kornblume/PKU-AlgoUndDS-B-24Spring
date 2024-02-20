def swap(x,y):
	x,y = y,x
	x[0],y[0] = y[0],x[0]
a = [1,2,3]
b = [4,5,6]
swap(a,b)
print(a)