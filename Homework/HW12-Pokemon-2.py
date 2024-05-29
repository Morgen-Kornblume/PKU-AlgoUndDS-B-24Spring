import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    dist = [1145141919810 for _ in range(len(graph))]
    dist[start] = 0
    vised = [False for _ in range(len(graph))]
    while len(queue) > 0:
        d, u = heapq.heappop(queue)
        if vised[u]:
            continue
        vised[u] = True
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(queue, (dist[v], v))
        
    return dist

def solve():
    N, M = map(int, input().split())
    time_to_defeat = [0, 0] + [int(input()) for _ in range(N)]
    graph = [[] for _ in range(N + 2)]
    for _ in range(M):
        u, v, t = map(int, input().split())
        graph[u].append((v, t+time_to_defeat[v]))
        graph[v].append((u, t+time_to_defeat[u]))
    dist = dijkstra(graph, 0)
    print(dist[1])

solve()