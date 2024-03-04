import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

# a와 b의 촌수를 계산해야 함
# 촌수 = a에서 시작하여 b까지 도달하는 거리
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)