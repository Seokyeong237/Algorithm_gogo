import sys
from collections import deque

input = sys.stdin.readline

n, m, start = map(int, input().split())

adj_list = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(n+1):
    adj_list[i].sort()

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    
    # 인접 리스트로 들어가기
    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in adj_list[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

dfs(start)
print()
visited = [False] * (n+1)
bfs(start)