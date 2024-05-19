"""
描述
现在有n个队伍参加了比赛，他们进行了m次PK。现在赛事方需要给他们颁奖（奖金为整数），已知参加比赛就可获得100元，由于比赛双方会比较自己的奖金，所以获胜方的奖金一定要比败方奖金高。请问赛事方要准备的最小奖金为多少？奖金数额一定是整数。

输入
一组数据，第一行是两个整数n(1≤n≤1000)和m(0≤m≤2000)，分别代表n个队伍和m次pk，队伍编号从0到n-1。接下来m行是pk信息，具体信息a，b，代表编号为a的队伍打败了编号为b的队伍。
输入保证队伍之间的pk战胜关系不会形成有向环
输出
给出最小奖金w
"""
# 拓扑排序
n, m = map(int, input().split())
in_degree = [0 for _ in range(n)]
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
q = []
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)
seq = []
while q:
    u = q.pop(0)
    seq.append(u)
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)
cash = [100 for _ in range(n)]
while len(seq) > 0:
    u = seq[-1]
    seq.pop()
    for v in graph[u]:
        cash[u] = max(cash[v] + 1, cash[u])
print(sum(cash))