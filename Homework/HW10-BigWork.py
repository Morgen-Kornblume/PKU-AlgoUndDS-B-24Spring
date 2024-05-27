#n nodes, m edges
#topsort
n, m = map(int, input().split())
#edge is directed
edges = [[] for i in range(n+1)]
cd = [0 for i in range(n+1)]
revedges = [[] for i in range(n+1)]
#indegree
indegree = [0 for i in range(n+1)]
#finish time
time = [0 for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    edges[a-1].append((b-1, c))
    #revedges[b].append((a, c))
    indegree[b-1] += 1
    #cd[a] += 1

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
print(max(time))
#print(stk)
if len(stk) < n:
    print("error")
    exit(0)
time2 = [max(time) for i in range(n+1)]
ans = []
#Crucial route in ans
while len(stk) > 0:
    x = stk[-1]
    stk.pop()
    for i in edges[x]:
        time2[x] = min(time2[x], time2[i[0]] - i[1])

#print(time)

#print(time2)

for i in range(n):
    for j in edges[i]:
        if time[i] == time2[j[0]] - j[1]:
            ans.append((i, j[0]))

ans.sort()
for i in ans:
    print("%d %d" % (i[0]+1, i[1]+1))