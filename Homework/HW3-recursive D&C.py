def binarySearch(a ,p,key = lambda x :x ):
	def search(L,R): #在a[L:R+1]范围内二分查找p
        # 在此处补充你的代码
		if(L == R):
			if(key(a[L]) == key(p)):
				return L
			else:
				return None
		mid = (L + R) // 2
		if key(a[mid]) >= key(p):
			return search(L,mid)
		else:
			return search(mid+1,R)
    #下面这一行是函数binarySearch的最后一条语句
	return search(0,len(a) - 1)
a = [9, 12, 27, 33, 33, 41, 80]  #a有序
print(binarySearch(a,33)) #>>3
print(binarySearch(a,57)) #>>None
a.sort(key = lambda x: x % 10)  #按个位数从小到大排序
print(a)    #>>[80, 41, 12, 33, 33, 27, 9]
print(binarySearch(a,57,key = lambda x: x %10)) #>>5