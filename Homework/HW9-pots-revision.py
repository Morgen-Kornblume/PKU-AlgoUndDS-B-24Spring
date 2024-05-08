va, vb, vc = map(int,input().split())

if va < vc and vb < vc:
    print("impossible")
    exit(0)

#  binary heap 小根堆
class binary_heap:
    def __init__(self):
        self.data = []
        self.size = 0

    def pos(self, x : int) -> int:
        return x - 1

    def top(self):
        return self.data[self.pos(1)]
    
    def push(self, x : any):
        self.size += 1
        self.data.append(x)
        self.upload(self.size)

    def upload(self, x : int):
        if x == 1:
            return
        if self.data[self.pos(x)] < self.data[self.pos(x//2)]:
            self.data[self.pos(x)], self.data[self.pos(x//2)] = self.data[self.pos(x//2)], self.data[self.pos(x)]
            self.upload(x//2)

    def pop(self):
        self.data[self.pos(1)] = self.data[self.pos(self.size)]
        self.size -= 1
        self.data.pop()
        self.download(1)
    
    def download(self, x : int):
        if x*2 > self.size:
            return
        if x*2 == self.size:
            if self.data[self.pos(x)] > self.data[self.pos(x*2)]:
                self.data[self.pos(x)], self.data[self.pos(x*2)] = self.data[self.pos(x*2)], self.data[self.pos(x)]
            return
        if self.data[self.pos(x*2)] < self.data[self.pos(x*2+1)]:
            if self.data[self.pos(x)] > self.data[self.pos(x*2)]:
                self.data[self.pos(x)], self.data[self.pos(x*2)] = self.data[self.pos(x*2)], self.data[self.pos(x)]
                self.download(x*2)
            else:
                return
        else:
            if self.data[self.pos(x)] > self.data[self.pos(x*2+1)]:
                self.data[self.pos(x)], self.data[self.pos(x*2+1)] = self.data[self.pos(x*2+1)], self.data[self.pos(x)]
                self.download(x*2+1)
            else:
                return
            
#将两个pot里面水的容量情况抽象成一个元组表示的状态
#然后使用dijskra算法处理，在处理时，记录下每个状态的前驱状态，最后根据前驱状态回溯出路径
#记录状态时直接生成答案字符串，不再额外记录路径

dist = [[114514 for i in range(101)] for j in range(101)]
dist[0][0] = 0
vis = [[0 for i in range(101)] for j in range(101)]
pre = [["" for i in range(101)] for j in range(101)]
q = binary_heap()
class node:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return dist[self.x][self.y] < dist[other.x][other.y]
    def __eq__(self, other):
        return dist[self.x][self.y] == dist[other.x][other.y]
    def __gt__(self, other):
        return dist[self.x][self.y] > dist[other.x][other.y]
q.push(node(0, 0))
while q.size:
    x = q.top().x
    y = q.top().y
    q.pop()
    if vis[x][y]:
        continue
    vis[x][y] = 1
    if not vis[va][y]:
        if dist[va][y] > dist[x][y] + 1:
            dist[va][y] = dist[x][y] + 1
            pre[va][y] = pre[x][y] + "FILL(1)\n"
            q.push(node(va, y))
    if not vis[x][vb]:
        if dist[x][vb] > dist[x][y] + 1:
            dist[x][vb] = dist[x][y] + 1
            pre[x][vb] = pre[x][y] + "FILL(2)\n"
            q.push(node(x, vb))
    if not vis[0][y]:
        if dist[0][y] > dist[x][y] + 1:
            dist[0][y] = dist[x][y] + 1
            pre[0][y] = pre[x][y] + "DROP(1)\n"
            q.push(node(0, y))
    if not vis[x][0]:
        if dist[x][0] > dist[x][y] + 1:
            dist[x][0] = dist[x][y] + 1
            pre[x][0] = pre[x][y] + "DROP(2)\n"
            q.push(node(x, 0))
    #对于POUR的情况，分类讨论，先把自己倒空还是对方先满
    if x + y <= va:
        if not vis[x+y][0]:
            if dist[x+y][0] > dist[x][y] + 1:
                dist[x+y][0] = dist[x][y] + 1
                pre[x+y][0] = pre[x][y] + "POUR(2,1)\n"
                q.push(node(x+y, 0))
    else:
        if not vis[va][x+y-va]:
            if dist[va][x+y-va] > dist[x][y] + 1:
                dist[va][x+y-va] = dist[x][y] + 1
                pre[va][x+y-va] = pre[x][y] + "POUR(2,1)\n"
                q.push(node(va, x+y-va))
    if x + y <= vb:
        if not vis[0][x+y]:
            if dist[0][x+y] > dist[x][y] + 1:
                dist[0][x+y] = dist[x][y] + 1
                pre[0][x+y] = pre[x][y] + "POUR(1,2)\n"
                q.push(node(0, x+y))
    else:
        if not vis[x+y-vb][vb]:
            if dist[x+y-vb][vb] > dist[x][y] + 1:
                dist[x+y-vb][vb] = dist[x][y] + 1
                pre[x+y-vb][vb] = pre[x][y] + "POUR(1,2)\n"
                q.push(node(x+y-vb, vb))
ans1 = 114514
ans2 = ""
for i in range(va+1):
    if dist[i][vc] < ans1:
        ans1 = dist[i][vc]
        ans2 = pre[i][vc]
for i in range(vb+1):
    if dist[vc][i] < ans1:
        ans1 = dist[vc][i]
        ans2 = pre[vc][i]
if ans1 == 114514:
    print("impossible")
else:
    print(ans1)
    print(ans2, end = "")