T = int(input())
mv = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
def traverse(x, y, vis, n, m, rem):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if vis[x][y] == 1:
        return 0
    if rem == 0:
        return 1
    vis[x][y] = 1
    ans = 0
    for (dx, dy) in mv:
        ans += traverse(x+dx, y+dy, vis, n, m, rem-1)
    vis[x][y] = 0
    return ans
while T > 0:
    n,m,x,y = map(int, input().split())
    vis = [[0 for i in range(m)] for j in range(n)]
    print(traverse(x, y, vis, n, m, n*m-1))
    T -= 1