import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

def dfs(s, graph, visited):
    global cnt
    visited[s] = cnt

    for i in graph[s]:
        if visited[i] == 0:
            cnt += 1
            dfs(i, graph, visited)

dfs(s, graph, visited)

for i in visited[1:]:
    print(i)