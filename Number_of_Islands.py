from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] =="1":
                    q.append((i, j))
                    ans += 1
                    grid[i][j] = "0"

                    while q:
                        size = len(q)
                        for k in range(size):
                            r,c = q.popleft()
                            
                            # UP
                            if r-1>=0 and grid[r-1][c]=="1":
                                grid[r-1][c]="0"
                                q.append((r-1,c))

                            # DOWN
                            if  r+1<m and grid[r+1][c]=="1":
                                grid[r+1][c]="0"
                                q.append((r+1,c))

                            # LEFT
                            if  c-1>=0 and grid[r][c-1]=="1":
                                grid[r][c-1]="0"
                                q.append((r,c-1))

                            # RIGHT
                            if  c+1<n and grid[r][c+1]=="1":
                                grid[r][c+1]="0"
                                q.append((r,c+1))
        return ans  