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