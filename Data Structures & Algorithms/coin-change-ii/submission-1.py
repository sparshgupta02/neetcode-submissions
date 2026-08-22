class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]* (amount+1)
        dp[0]=1

        for coin in coins:
            for s in range(1,amount+1):
                dp[s]+= dp[s-coin] if coin<=s else 0
        return dp[amount]