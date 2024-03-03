import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

maps = []
result = []

# 오른쪽, 왼쪽, 아래, 위, 대각선 오른쪽 위, 대각선 왼쪽 아래, 대각선 왼쪽 위, 대각선 오른쪽 아래
dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and maps[nx][ny] == 1:
            dfs(nx, ny)

def start(h, w):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] == 1:
                cnt += 1
                dfs(i, j)
    return cnt

while True: 
    w, h = map(int, input().split())
    if (h == 0 and w == 0):
        break
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        maps.append(list(map(int, input().split())))

    result.append(start(h, w))
    maps = []

for i in result:
    print(i)
