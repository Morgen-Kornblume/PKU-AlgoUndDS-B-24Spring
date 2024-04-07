# 实现一个类：带有按秩合并和路径压缩的并查集

class DisjointUnionSet:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

while True:
    try:
        n, m = map(int, input().split())
        bcj = DisjointUnionSet(n)
        for i in range(m):
            a, b = map(int, input().split())
            ans = bcj.merge(a - 1, b - 1)
            if ans:
                print("No")
            else:
                print("Yes")
        #创建一个字典，用于存储每个元素的根节点
        dic = {}
        for i in range(n):
            fa = bcj.find(i)
            if fa not in dic:
                dic[fa] = 1
            else:
                dic[fa] += 1
        print(len(dic))
        #输出总共有哪些根节点，从小到大，在dic中的键值
        ans = list(dic.keys())
        #print(ans)
        ans.sort()
        for i in ans:
            print(i + 1, end = "")
            if i != ans[-1]:
                print(" ", end = "")
        print()
    except EOFError:
        break