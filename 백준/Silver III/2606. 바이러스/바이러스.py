import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

computer = int(input())
m = int(input())

adj_list = [[] for _ in range(computer+1)]
visited = [False] * (computer+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def dfs(v):
    global count
    visited[v] = True
    for i in adj_list[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            count += 1

dfs(1)
print(count)