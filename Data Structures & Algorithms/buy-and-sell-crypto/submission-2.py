class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        k=len(prices)
        min_till_now=[]
        min_now=prices[0]
        min_till_now.append(min_now)
        for i in range(1,k):
            min_now=min(min_now,prices[i])
            min_till_now.append(min_now)
            curr=max(0,prices[i]-min_till_now[i])
            res=max(curr,res)

        return res