import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

maps = [list(map(str, input().split())) for _ in range(5)]
# 아레, 위, 오른쪽, 왼쪽
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

def dfs(x, y, number):
    if len(number) == 6:
        if number not in answer:
            answer.append(number)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, number+maps[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, maps[i][j])

print(len(answer))