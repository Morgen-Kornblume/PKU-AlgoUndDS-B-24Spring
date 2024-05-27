"""
描述
VR国有着复杂的地下网络，由n个站点和m条通道组成了一个简单连通图。由于每条通道的建设成本不尽相同，所以它们有着不同的价值。特工小z在VR国潜伏多年，某天她半夜拿了个快递，原来是个环状发生器！她读起了环状发生器的说明书：

环状发生器可以使用任意多次。每次使用环状发生器，你需要指定地下网络中一个由未被破坏的通道组成的环。然后你可以指定环上的任意一条通道，让它永久地被破坏。

收到了如此强大的武器，小z高兴地说：“太破费了！好久没有收到这么贵重的礼物了！”。但她转念又说：“坏了坏了坏了，我不知道怎么样用才能让VR国的地下网络遭到最大的破坏！”这时你自告奋勇地站出来，说：

你知道怎么样用环状发生器，可以让VR国被破坏的通道价值总和最大。

请注意，小Z对道路一条条地破坏，一旦发现无环，就会停止破坏。

听到你愿意为她解决这个难题，她感激地说：“谢谢你啊谢谢你，红豆泥塞克油买了西！”

输入
第一行两个正整数，n和m，分别代表VR国地下网络的站点数和通道数，站点的编号为从0到n-1。

接下来m行，每行三个整数x, y和v，表示通道连接的两个站点编号，以及这条通道的价值。

数据范围 0< n, m < 100000

|v|<1,000,000,000
输出
一行一个整数，代表最大的破坏价值总和。
"""

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
    
n, m = map(int, input().split())
edges = []
for _ in range(m):
    x, y, v = map(int, input().split())
    edges.append((x, y, v))
edges.sort(key=lambda x: x[2])
dsu = DisjointUnionSet(n)
ans = 0
for x, y, v in edges:
    if dsu.merge(x, y) == False:
        ans += v
print(ans)