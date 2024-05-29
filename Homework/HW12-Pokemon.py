class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
    #Define all the comparison operators
    def __lt__(self, other):
        return self.data < other.data
    def __le__(self, other):
        return self.data <= other.data
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        return self.data != other.data
    def __gt__(self, other):
        return self.data > other.data
    def __ge__(self, other):
        return self.data >= other.data

class BinaryHeap:
    '''
    二叉堆模板，默认为大根堆
    '''
    def __init__(self):
        self.dat = []
        self.size = 0
    
    def upload(self, nowa):
        '''
        向上调整节点（大根堆）
        '''
        x = nowa
        while(x > 1 and self.dat[x-1].data > self.dat[(x // 2)-1].data):
            self.dat[x-1], self.dat[(x // 2)-1] = self.dat[(x // 2)-1], self.dat[x-1]
            x = x // 2

    def insert(self, data):
        '''
        插入一个新的点，数据为 data（data必须可以比较）
        '''
        self.size += 1
        self.dat.append(data)
        self.upload(self.size)

    def download(self):
        '''
        删除堆顶后向下调整
        '''
        nowa = 1
        while(nowa * 2 <= self.size):
            tmp = nowa * 2
            if(tmp + 1 <= self.size and self.dat[tmp] > self.dat[tmp-1]):
                t += 1
            if(self.dat[tmp-1] < self.dat[nowa-1]):
                break
            self.dat[tmp-1], self.dat[nowa-1] = self.dat[nowa-1], self.dat[tmp-1]
            nowa = tmp

    def pop(self):
        '''
        弹出堆顶元素
        '''
        if(self.size > 0):
            self.dat[0], self.dat[self.size-1] = self.dat[self.size-1], self.dat[0]
            self.dat.pop()
            self.size -= 1
            self.download()

    def top(self):
        '''
        返回堆顶元素
        '''
        if(self.size > 0):
            return self.dat[0]
        else :
            return None
# DJS算法，最短路，分层图

n, m = map(int, input().split())
pokemon = []
for i in range(n):
    pokemon.append(int(input()))
pokemon.append(0)
pokemon.append(0)
s = n 
t = (n+1) 
edges = [ [] for i in range((n+2)*2) ]
for i in range (m):
    u, v, w = map(int, input().split())
    if u == 0:
        u = s
    elif u == 1:
        u = t
    else:
        u = u-2
    if v == 0:
        v = s
    elif v == 1:
        v = t
    else:
        v = v-2
    edges[u*2].append((v*2, w))
    edges[u*2+1].append((v*2+1, w))
    edges[v*2].append((u*2, w))
    edges[v*2+1].append((u*2+1, w))
    
for i in range(n):
    edges[i*2].append((i*2+1, pokemon[i]))
    edges[i*2+1].append((i*2, 0))

# Dijkstra

dist = [1145141919810 for i in range((n+2)*2)]

dist[s*2] = 0
visited = [False for i in range((n+2)*2)]

heap = BinaryHeap()

heap.insert(Node(-dist[s*2], s*2))

while heap.size > 0:
    top = heap.top()
    heap.pop()
    dis = -top.key
    now = top.data
    print(now, dis)
    if visited[now]:
        continue
    visited[now] = True
    for i in edges[now]:
        to = i[0]
        w = i[1]
        if dist[to] > dist[now] + w:
            dist[to] = dist[now] + w
            heap.insert(Node(-dist[to], to))

print(dist[t*2])