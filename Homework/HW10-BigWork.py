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
<<<<<<< HEAD
    print("%d %d" % (i[0]+1, i[1]+1))
=======
    print("%d %d" % (i[0], i[1]))

'''
中国要在火星上搞个大工程，即建造n个科考站

建科考站需要很专业的设备，不同的科考站需要不同的设备来完成

有的科考站必须等另外一些科考站建好后才能建。

每个设备参与建完一个科考站后，都需要一定时间来保养维修，才能参与到下一个科考站的建设。

所以，会发生科考站A建好后，必须至少等一定时间才能建科考站B的情况。因为B必须在A之后建，且建B必需的某个设备，参与了建A的工作，它需要一定时间进行维修保养。

一个维修保养任务用三个数a b c表示，意即科考站b必须等a建完才能建。而且，科考站a建好后，建a的某个设备必须经过时长c的维修保养后，才可以开始参与建科考站b。

假设备都很牛，只要设备齐全可用，建站飞快就能完成，建站时间忽略不计。一开始所有设备都齐全可用。

给定一些维修保养任务的描述，求所有科考站都建成，最快需要多长时间。

有的维修保养任务，能开始的时候也可以先不开始，往后推迟一点再开始也不会影响到整个工期。问在不影响最快工期的情况下，哪些维修保养任务的开始时间必须是确定的。按字典序输出这些维修保养工任务，输出的时候不必输出任务所需的时间

输入
第一行两个整数n,m，表示有n个科考站，m个维修保养任务。科考站编号为1，2.....n
接下来m行，每行三个整数a b c，表示一个维修保养任务
1 < n,m <=3000
输出
先输出所有科考站都建成所需的最短时间
然后按字典序输出开始时间必须确定的维修保养任务
样例输入
9 11
1 2 6
1 3 4
1 4 5
2 5 1
3 5 1
4 6 2
5 7 9
5 8 7
6 8 4
7 9 2
8 9 4
样例输出
18
1 2
2 5
5 7
5 8
7 9
8 9
'''
>>>>>>> f235f6eb60ff4402fddc06d1dd2af8bd1daa3c60
