class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def dfs(i):
            if dp[i]!=-1:
                return dp[i]
            
            num=1
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    num=max(num,1+dfs(j))

            dp[i]=num            
            return num

        return max(dfs(i) for i in range(n))