import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    answer = []
    global days
    days = 0
    flag = False
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def dfs(x, y):
        global days
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] != "X":
                # print("nx: ", nx)
                # print("ny: ", ny)
                # print(maps[nx][ny])
                days += int(maps[nx][ny])
                #print("days: ", days)
                dfs(nx, ny)
          
    for i in range(n):
        for j in range(m):
            days = 0
            if not visited[i][j] and maps[i][j] != "X":
                flag = True
                days += int(maps[i][j])
                dfs(i, j)
                answer.append(days)
                
    if not flag:
        return [-1]
    
    answer.sort()
    return answer