exit = None
def times(n):
## 在此处补充你的代码
	ans = 0
	while True:
		yield ans
		ans += n
		
n,m = map(int,input().split())
seq = times(n)
if str(type(seq) == "<class 'generator'>"):
	i = 0
	for x in seq:
		print(x)
		i += 1
		if i == m:
			break