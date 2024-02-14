class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        count = 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        # 아래, 위, 오른쪽, 왼쪽
        
        def dfs(x, y):
            visited[x][y] = True
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] == "1":
                    dfs(nx, ny)

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count +=1

        return count

        