class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        q = collections.deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        di = [(-1,0), (0,-1), (1,0), (0,1)]

        while q:
            i, j = q.popleft()

            for a, b in di:
                ni, nj = i+a, j+b

                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue

                if grid[ni][nj] != 2147483647:
                    continue

                grid[ni][nj] = grid[i][j] + 1
                q.append((ni, nj))