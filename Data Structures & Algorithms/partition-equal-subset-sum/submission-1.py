class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        for num in nums:
            s += num

        if s % 2 != 0:
            return False

        req = s // 2
        dp = {}

        def dfs(i, cursum):
            if cursum == req:
                return True

            if i == len(nums):
                return False

            if (i, cursum) in dp:
                return dp[(i, cursum)]

            # take
            if cursum + nums[i] <= req:
                b1 = dfs(i + 1, cursum + nums[i])
            else:
                b1 = False

            # don't take
            b2 = dfs(i + 1, cursum)

            dp[(i, cursum)] = b1 or b2
            return dp[(i, cursum)]

        return dfs(0, 0)