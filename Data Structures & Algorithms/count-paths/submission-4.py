class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[1][1]=1

        def dfs(i,j):
            if(i<=0 or i>m or j<=0 or j>n):
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            dp[i][j]= dfs(i-1,j)+dfs(i,j-1)
            return dp[i][j]

        return dfs(m,n)        


