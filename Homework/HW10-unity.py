class DisjointUnionSet:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        self.parent[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

#n people and m pairs of friends with a cost to make them friends
#calculate the minimum cost to make everyone friends
#output the cost and the pairs of friends
#use Kruskal's algorithm
n, m = map(int, input().split())
edges = []
#cost is float
#people code is int
for i in range(m):
    a, b, c = input().split()
    edges.append((float(c), int(a), int(b)))
edges.sort()

bcj = DisjointUnionSet(n)
ans = []
cost = 0.0
tot = 0
for edge in edges:
    if bcj.merge(edge[1], edge[2]):
        cost += edge[0]
        ans.append((edge[1], edge[2]))
        tot += 1
if tot < n - 1:
    print("NOT CONNECTED")
    exit(0)
print("%.2f" % cost)
#split by space
for i in ans:
    print("%d %d" % (i[0], i[1]))