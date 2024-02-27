class A:
	def __init__(self,x):
		self.x = x
	def __lt__(self,other):
		#实现小于号
		if(isinstance(other,int)):
			return self.x < other
		return self.x < other.x
	def __ge__(self,other):
		#实现大于等于号
		return self.x >= other.x
	
a,b,c = map(int,input().split())
print(isinstance(A(2),A))
print(A(a) < A(b))
print(A(a) >= A(c))
print(A(a) < c) 