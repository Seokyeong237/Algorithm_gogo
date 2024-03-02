from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    # 아래, 위, 오른쪽, 왼쪽
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny)) 
        return maps[n-1][m-1]
        
    answer = bfs(0, 0)
    if answer == 1:
        answer = -1
        
    return answer

    