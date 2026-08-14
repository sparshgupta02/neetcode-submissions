class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])

        visit = set()
        res=0

        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            res=0

            while q:
                row,col = q.popleft()
                grid[r][c] = 0
                res+=1
                di = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in di:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= cols or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    ar=bfs(r,c)
                    res=max(ar,res)
        return res