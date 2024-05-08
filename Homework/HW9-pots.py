class BinaryHeap:
    '''
    二叉堆模板，默认为大根堆
    '''
    def __init__(self, data0):
        self.dat = [data0]
        self.size = 1
    
    def upload(self, nowa):
        '''
        向上调整节点（大根堆）
        '''
        x = nowa
        while(x > 1 and self.dat[x].data > self.dat[x // 2].data):
            self.dat[x], self.dat[x // 2] = self.dat[x // 2], self.dat[x]
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
            if(tmp + 1 <= self.size and self.dat[tmp + 1] > self.dat[tmp]):
                t += 1
            if(self.dat[tmp] < self.dat[nowa]):
                break
            self.dat[tmp], self.dat[nowa] = self.dat[nowa], self.dat[tmp]
            nowa = tmp

    def pop(self):
        '''
        弹出堆顶元素
        '''
        if(self.size > 0):
            self.dat[1], self.dat[self.size] = self.dat[self.size], self.dat[1]
            self.dat.pop()
            self.size -= 1
            self.download()

    def top(self):
        '''
        返回堆顶元素
        '''
        return self.dat[1]

va, vb, vc = map(int, input().split())
#status A liters in A, B liters in B
#Target C liters in A or B
if va < vc and vb < vc:
    print("Impossible")
    exit(0)
vis = [[0 for i in range(101)] for j in range(101)]
dist = [[114514 for i in range(101)] for j in range(101)]
dist[0][0] = 0
# Implementing Dijkstra Algorithm

class node:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.key = c
    #define the comparison method < = >
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key <= other.key
    def __gt__(self, other):
        return self.key > other.key
    def __ge__(self, other):
        return self.key >= other.key
    def __eq__(self, other):
        return self.key == other.key
    
heap = BinaryHeap(node(0, 0, 0))
heap.insert(node(0, 0, 0))
while heap.size > 1:
    now = heap.top()
    now.key = -now.key
    heap.pop()
    if vis[now.a][now.b]:
        continue
    vis[now.a][now.b] = 1
    #fill A
    if not vis[va][now.b]:
        dist[va][now.b] = min(dist[va][now.b], now.key + 1)
        heap.insert(node(va, now.b, -dist[va][now.b]))
    #fill B
    if not vis[now.a][vb]:
        dist[now.a][vb] = min(dist[now.a][vb], now.key + 1)
        heap.insert(node(now.a, vb, -dist[now.a][vb]))
    #empty A
    if not vis[0][now.b]:
        dist[0][now.b] = min(dist[0][now.b], now.key + 1)
        heap.insert(node(0, now.b, -dist[0][now.b]))
    #empty B
    if not vis[now.a][0]:
        dist[now.a][0] = min(dist[now.a][0], now.key + 1)
        heap.insert(node(now.a, 0, -dist[now.a][0]))
    #pour A to B
    if now.a + now.b > vb:
        if not vis[now.a + now.b - vb][vb]:
            dist[now.a + now.b - vb][vb] = min(dist[now.a + now.b - vb][vb], now.key + 1)
            heap.insert(node(now.a + now.b - vb, vb, -dist[now.a + now.b - vb][vb]))
    else:
        if not vis[0][now.a + now.b]:
            dist[0][now.a + now.b] = min(dist[0][now.a + now.b], now.key + 1)
            heap.insert(node(0, now.a + now.b, -dist[0][now.a + now.b]))
    #pour B to A
    if now.a + now.b > va:
        if not vis[va][now.a + now.b - va]:
            dist[va][now.a + now.b - va] = min(dist[va][now.a + now.b - va], now.key + 1)
            heap.insert(node(va, now.a + now.b - va, -dist[va][now.a + now.b - va]))
#output the result
ans = 114514
for i in range(101):
    ans = min(ans, dist[i][vc], dist[vc][i])
if ans == 114514:
    print("Impossible")
else:
    print(ans)