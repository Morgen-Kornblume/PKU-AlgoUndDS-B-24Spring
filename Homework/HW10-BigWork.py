#n nodes, m edges
#topsort
n, m = map(int, input().split())
#edge is directed
edges = [[] for i in range(n+1)]
revedges = [[] for i in range(n+1)]
#indegree
indegree = [0 for i in range(n+1)]
#finish time
time = [0 for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    revedges[b].append((a, c))
    indegree[b] += 1

q = []
stk = []
for i in range(n):
    if indegree[i] == 0:
        q.append(i)
while len(q) > 0:
    x = q.pop(0)
    stk.append(x)
    for i in edges[x]:
        indegree[i[0]] -= 1
        time[i[0]] = max(time[i[0]], time[x] + i[1])
        if indegree[i[0]] == 0:
            q.append(i[0])
print(time[stk[-1]])
flg = [0 for i in range(n+1)]
flg[stk[-1]] = 1
ans = []
while len(stk) > 0:
    x = stk.pop()
    for i in revedges[x]:
        if time[i[0]] == time[x] - i[1] and flg[x] == 1:
            flg[i[0]] = 1
            ans.append((i[0], x))
ans.sort()
for i in ans:
    print("%d %d" % (i[0], i[1]))
