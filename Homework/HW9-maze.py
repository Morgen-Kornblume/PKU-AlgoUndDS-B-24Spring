a, b = map(int, input().split())
#输入一个二维数组，表示迷宫
maze = [list(input()) for i in range(a)]
#记录每个状态的前驱状态，用于回溯路径，由于需要不换行地输出路径，所以直接记录答案字符串
pre = [["" for j in range(b)] for i in range(a)]
#使用BFS搜索最短路径
q = []
vis = [[0 for j in range(b)] for i in range(a)]
#初始状态
q.append((0, 0))
while len(q) > 0:
    x, y = q.pop(0)
    vis[x][y] = 1
    if x == a - 1 and y == b - 1:
        break
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x + i < a and 0 <= y + j < b and maze[x + i][y + j] == '.' and vis[x + i][y + j] == 0:
            q.append((x + i, y + j))
            pre[x + i][y + j] = pre[x][y] + "(%d,%d)" % (x, y)
#回溯路径
if vis[a - 1][b - 1] == 0:
    print("0")
else:
    print(pre[a - 1][b - 1] + "(%d,%d)" % (a - 1, b - 1))