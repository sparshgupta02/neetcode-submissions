class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        def capture(r,c):
            if (r < 0 or c < 0 or r == n or c == m or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
    
        for i in range(n):
            if board[i][0]=="O":
                capture(i,0)
            if board[i][m-1] == "O":
                capture(i, m - 1)
        for j in range(m):
            if board[0][j]=="O":
                capture(0,j)
            if board[n-1][j]=="O":
                capture(n-1,j)
        for r in range(n):
            for c in range(m):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"
