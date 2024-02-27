class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next

class LinkList:
	def __init__(self):
		self.head = None

	def initList(self, data):
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next

	def insertCat(self):
# 在此处补充你的代码
		size = 0
		ptr = self.head
		while ptr is not None:
			size += 1
			ptr = ptr.next
		pos = (size + 1) // 2
		ptr = self.head
		while pos != 1:
			ptr = ptr.next
			pos -= 1
		nd = Node(6, ptr.next)
		ptr.next = nd
########            
	def printLk(self):
		p = self.head
		while p:
			print(p.data, end=" ")
			p = p.next
		print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()