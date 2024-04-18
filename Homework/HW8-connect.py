def traverse(nowa, node, vis): 
    vis[nowa] = 1
    for i in node[nowa]:
        if(vis[i] == 0):
            traverse(i, node, vis)
    return

n,m = map(int, input().split())
vis = [0 for i in range(n)]
node = [[] for _ in range(n)]
#print(node)
for i in range(m):
    u,v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
traverse(0, node, vis)
for i in range(n):
    if(vis[i] == 0):
        print('no')
        exit()
print('yes')