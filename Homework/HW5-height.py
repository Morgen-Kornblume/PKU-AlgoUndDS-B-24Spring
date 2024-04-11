ht = 0
son = []

def traverse(node, height):
    global ht
    global son
    if(node == -1):
        return
    ht = max(ht, height)
    traverse(son[node][0], height+1)
    traverse(son[node][1], height+1)
    return

n = int(input())


leaf = 0

for i in range(n):
    u,v = input().split()
    son.append((int(u),int(v)))
    if(u == "-1" and v == "-1"):
        leaf += 1

for i in range(n):
    traverse(i, 0)

print("%d %d" % (ht, leaf), end="")