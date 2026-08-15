class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh=0
        time=0
        q = collections.deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j]==1:
                    fresh+=1

        di = [(-1,0), (0,-1), (1,0), (0,1)]

        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                i, j = q.popleft()

                for a, b in di:
                    ni, nj = i+a, j+b

                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue

                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh-=1
                        q.append((ni,nj))
            time+=1
        return time if fresh==0 else -1

        